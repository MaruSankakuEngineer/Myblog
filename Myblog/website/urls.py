from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('about', views.about, name='about'),
    
]
