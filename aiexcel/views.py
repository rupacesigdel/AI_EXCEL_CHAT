from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .mindsdb_tools import predict_with_mindsdb
import logging, requests
from django.conf import settings
from .models import ExcelKnowledge,Excelchat
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

logger = logging.getLogger(__name__)

GEMINI_API_KEY = settings.GEMINI_API_KEY
GEMINI_API_URL = settings.GEMINI_API_URL

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
    

def chat_bot(request):
    user_query = request.GET.get('query', '')
    logger.debug(f"User query: {user_query}")
    if not user_query:
        return JsonResponse({'error': 'No query provided'}, status=400)

    try:
        search_vector = SearchVector('question', 'answer')
        search_query = SearchQuery(user_query)
        search_results = Excelchat.objects.annotate(
            search=search_vector
        ).filter(search=search_query)

        if search_results.exists():
            result = search_results.first()
            return JsonResponse({'answer': result.answer})

        # Replace OpenAI API call with Gemini API call
        headers = {
            'Authorization': f'Bearer {GEMINI_API_KEY}',
            'Content-Type': 'application/json',
        }
        data = {
            'contents': [
                {'parts': [{'text': f"Answer the following Excel question: {user_query}"}]}
            ]
        }
        response = requests.post(GEMINI_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        response_data = response.json()

        logger.debug(f"Gemini response: {response_data}")

        # Check if 'answer' is in the response_data
        answer = response_data.get('contents', [{'parts': [{'text': 'No answer found'}]}])[0]['parts'][0].get('text', 'No answer found')
        return JsonResponse({'answer': answer})

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
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