from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import BlogEntry

def splash(request):
    return render(request, 'website/splash.html', {})

def index(request):
    return render(request, 'website/home.html', {})

def my_work_music(request):
    return render(request, 'website/my-work-music.html', {})

def my_work_code(request):
    return render(request, 'website/my-work-code.html', {})

def bio(request):
    return render(request, 'website/bio.html', {})

def lessons(request):
    return render(request, 'website/lessons.html', {})

def blog_entry_detail(request, id):
    entry = get_object_or_404(BlogEntry, id=id)
    return render(request, 'website/entry.html', {'entry': entry})
