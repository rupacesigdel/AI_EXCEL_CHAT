from django.db import models
from django.contrib.auth.models import User
import json
from django.db.models import JSONField

class ExcelKnowledge(models.Model):
    category = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        db_table = 'aiexcel_excelknowledge'

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = JSONField()  # Use JSONField for both PostgreSQL and SQLite
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat from {self.user.username} on {self.created_at}"

class AIModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name