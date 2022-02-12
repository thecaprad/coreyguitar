from django.contrib import admin
from .models import BlogEntry, Show, Venue

admin.site.register(BlogEntry)
admin.site.register(Show)
admin.site.register(Venue)
