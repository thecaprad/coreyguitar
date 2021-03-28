from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'website/splash.html', {})

def home(request):
    return render(request, 'website/home.html', {})
