from django.shortcuts import render, redirect
from .models import FormSubmission
from datetime import datetime

def home(request):
    current_time = datetime.now()
    return render(request, 'home.html', {'current_time': current_time})

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        submission = FormSubmission(name=name, email=email)
        submission.save()

        return redirect('submissions')

    return render(request, 'form.html')

def submissions_view(request):
 
    submissions = FormSubmission.objects.all()
    return render(request, 'submissions.html', {'submissions': submissions})
