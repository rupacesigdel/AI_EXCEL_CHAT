from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField
from django.core.exceptions import ValidationError


class ExcelKnowledge(models.Model):
    category = models.CharField(max_length=50)
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        db_table = 'aiexcel_excelknowledge'


class Excelchat(models.Model):
    CATEGORY_CHOICES = [
        ('Formula', 'Formula'),
        ('Rule', 'Rule'),
        ('Syntax', 'Syntax'),
        ('Project Idea', 'Project Idea'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, db_index=True)
    question = models.TextField(db_index=True)
    answer = models.TextField()

    def clean(self):
        if not self.question or not self.answer:
            raise ValidationError('Both question and answer fields must be filled.')

    def __str__(self):
        return f"{self.category}: {self.question[:50]}"

    class Meta:
        verbose_name = "Excel chat"
        verbose_name_plural = "Excel chat"
        ordering = ['category']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['question']),
        ]

class ChatHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat from {self.user.username} on {self.created_at}"

class AIModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name