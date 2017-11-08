from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def job_detail(request, id):
    return render(request, 'job_detail.html', {})
