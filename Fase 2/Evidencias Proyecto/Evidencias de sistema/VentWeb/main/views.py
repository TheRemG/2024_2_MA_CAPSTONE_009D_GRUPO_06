from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logon(request):
    return render(request, 'logon.html')

def perfil(request):
    return render(request, 'perfil.html')

def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistroForm()
        
    return render(request, "logon.html", {"form": form})
# Create your views here.
