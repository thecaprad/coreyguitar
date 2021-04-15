from django.http import HttpResponse
from django.shortcuts import render

def splash(request):
    return render(request, 'website/splash.html', {})

def index(request):
    return render(request, 'website/home.html', {})

def my_work(request):
    return render(request, 'website/my-work.html', {})
