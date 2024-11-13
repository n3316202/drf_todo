from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSimpleSerializer,TodoCreateSerializer

class TodosAPIView(APIView):
    
    def get(self, request):
        todos = Todo.objects.filter(complete=False) 
        serializer = TodoSimpleSerializer(todos, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)