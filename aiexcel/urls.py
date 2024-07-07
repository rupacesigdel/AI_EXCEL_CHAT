
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import get_excel_knowledge

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('get-excel-knowledge/', get_excel_knowledge, name='get_excel_knowledge'),
    path('login/', auth_views.LoginView.as_view(template_name='aiexcel/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='aiexcel/password_reset.html'), name='password_reset'),
]
