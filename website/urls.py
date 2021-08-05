from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('my-work-music/', views.my_work_music, name='my_work_music'),
    path('my-work-code/', views.my_work_code, name='my_work_code'),
    path('bio/', views.bio, name='bio'),
    path('lessons/', views.lessons, name='lessons'),
    path('blog/<int:id>/', views.blog_entry_detail, name='blog_entry_detail')
]