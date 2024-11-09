from django.shortcuts import render,redirect
"""from .forms import RegistroForm"""
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logon(request):
    return render(request, 'logon.html')

"""
def logon(request):
    if request.method == "GET":
        return render(request, 'logon.html', {
            'form': UserCreationForm
        })
    else:
        user = User.objects.create_user()"""