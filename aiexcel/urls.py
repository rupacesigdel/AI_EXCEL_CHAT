
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import chat_bot

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('chat-bot/',chat_bot, name='chat_bot'),
    path('login/', auth_views.LoginView.as_view(template_name='aiexcel/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='aiexcel/password_reset.html'), name='password_reset'),
]
