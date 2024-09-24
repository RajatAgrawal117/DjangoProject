from django.shortcuts import render
from datetime import datetime

def home(request):
    current_time = datetime.now()
    return render(request, 'home.html', {'current_time': current_time})
