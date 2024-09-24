from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
def home(request):
    current_time = datetime.now()
    return render(request, 'home.html', {'current_time': current_time})


def submit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        return HttpResponse(f"Received: {name}, {email}")
    return HttpResponse("Invalid method.")
