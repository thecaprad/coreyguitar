from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import BlogEntry

def splash(request):
    return render(request, 'website/splash.html', {})

def index(request):
    return render(request, 'website/home.html', {})

def my_work(request):
    return render(request, 'website/my-work.html', {})

def bio(request):
    return render(request, 'website/bio.html', {})

def blog_entry_detail(request, id):
    entry = get_object_or_404(BlogEntry, id=id)
    return render(request, 'website/entry.html', {'entry': entry})
