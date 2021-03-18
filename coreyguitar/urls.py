from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('website/', include('website.urls')),
    path('admin/', admin.site.urls),
]