from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def services(request):
    return render(request, 'home/services.html')

def document(request):
    return render(request, 'home/document.html')