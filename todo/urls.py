from django.contrib import admin
from django.urls import include, path
from .views import  TodosAPIView

urlpatterns = [
    path('', TodosAPIView.as_view()),
]
