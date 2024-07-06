from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .mindsdb_tools import predict_with_mindsdb
import logging

logger = logging.getLogger(__name__)

@login_required
def home(request):
    return render(request, 'aiexcel/home.html')

@login_required
@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if user_message:
            try:
                ai_reply = predict_with_mindsdb(user_message)
                
                if 'error' in ai_reply:
                    return JsonResponse({"error": ai_reply['error']}, status=500)

                return JsonResponse({"reply": ai_reply.get('answer', 'No response from model.')})
            except Exception as e:
                logger.error("Error in chat view: %s", str(e))
                return JsonResponse({"error": str(e)}, status=500)
        return JsonResponse({"error": "No message provided"}, status=400)
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