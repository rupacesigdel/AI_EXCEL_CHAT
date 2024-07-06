from django.contrib import admin
from .models import ChatHistory, AIModel

@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'response', 'created_at')
    search_fields = ('user__username', 'message', 'response')
    list_filter = ('created_at',)

@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')