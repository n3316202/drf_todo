from django.contrib import admin
from django.urls import include, path
from .views import  TodosAPIView, TodoAPIView

urlpatterns = [
    path('', TodosAPIView.as_view()),
    path('<int:pk>/', TodoAPIView.as_view()),    
]
