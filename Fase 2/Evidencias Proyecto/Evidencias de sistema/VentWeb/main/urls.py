from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logon/', views.logon, name='logon'),
    path('perfil/', views.perfil, name='perfil'),
    path('index/', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
]