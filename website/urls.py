from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('my-work/', views.my_work, name='my_work'),
    path('blog/<int:id>/', views.blog_entry_detail, name='blog_entry_detail')
]