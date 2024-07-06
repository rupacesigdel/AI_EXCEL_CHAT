from django.db import models
from django.contrib.auth.models import User
import json

# Import the new JSONField from django.db.models
from django.db.models import JSONField

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