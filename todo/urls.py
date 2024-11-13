from django.contrib import admin
from django.urls import include, path
from .views import TodoAPIView, TodosAPIView

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),
]
