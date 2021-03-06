from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
import datetime
from .models import BlogEntry, Show, Venue

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

def blog(request):
    entries = BlogEntry.objects.all().order_by('-date')
    return render(request, 'website/blog.html', {'entries': entries})

def blog_entry_detail(request, id):
    entry = get_object_or_404(BlogEntry, id=id)
    if entry.is_draft:
        return redirect('website:index')
    if entry.url != request.path:
        return redirect(entry.url)
    return render(request, 'website/entry.html', {'entry': entry})

def shows(request):
    today = timezone.now() - datetime.timedelta(hours=6)
    shows = Show.objects.filter(date__gte=today).order_by('date')
    return render(request, 'website/shows.html', {'shows': shows})
