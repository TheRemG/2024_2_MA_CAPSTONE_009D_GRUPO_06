from django.shortcuts import render
from .forms import ClienteForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def logon(request):
    usuario = ClienteForm()
    return render(request, 'logon.html', {'form': ClienteForm})

