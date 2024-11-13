from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # 생성 될때
    updated_at = models.DateTimeField(auto_now=True) # 업데이트 될때 

    def __str__(self):
        return self.title