from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .mindsdb_tools import predict_with_mindsdb
import logging
from .models import ExcelKnowledge


logger = logging.getLogger(__name__)

@login_required
def home(request):
    return render(request, 'aiexcel/home.html')

@login_required
@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        # Fetch the relevant answer from ExcelKnowledge model
        try:
            knowledge = ExcelKnowledge.objects.filter(question__icontains=user_message).first()
            if knowledge:
                response = knowledge.answer
            else:
                response = "I'm sorry, I don't have an answer for that question."
        except Exception as e:
            response = f"An error occurred: {str(e)}"

        return JsonResponse({'reply': response})

    return render(request, 'aiexcel/chat.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'aiexcel/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')