from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .mindsdb_tools import predict_with_mindsdb
import logging, openai
from django.conf import settings
from .models import ExcelKnowledge,Excelchat

openai.api_key = settings.OPENAI_API_KEY
logger = logging.getLogger(__name__)

@login_required
@csrf_exempt
def home(request):
    return render(request, 'aiexcel/home.html')

@login_required
@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
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
    
@login_required
@csrf_exempt
def get_excel_knowledge(request):
    user_query = request.GET.get('query', '')
    if not user_query:
        return JsonResponse({'error': 'No query provided'}, status=400)
    
    try:
        knowledge = Excelchat.objects.filter(question__icontains=user_query).first()
        if knowledge:
            return JsonResponse({'answer': knowledge.answer})

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Answer the following Excel question: {user_query}",
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        return JsonResponse({'answer': answer})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

@login_required
@csrf_exempt
def chatbot(request):
    return render(request, 'aiexcel/chatbot.html')

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