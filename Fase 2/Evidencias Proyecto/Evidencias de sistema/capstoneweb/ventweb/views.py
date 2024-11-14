from django.shortcuts import render, redirect
from .forms import ClienteForm, LoginForm
from django.contrib import messages
from .models import Usuario

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logon(request):
    if request.method == 'POST':
        usuario = ClienteForm(request.POST)
        if usuario.is_valid():
            usuario.save()
            messages.success(request, "Usuario registrado con exito")
            return redirect('index')
    else: 
        usuario = ClienteForm()
    return render(request, 'logon.html', {'form': usuario})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']

            try:
                user = Usuario.objects.get(rut=rut)
                if user.password == password:
                    request.session['usuario_id'] = user.rut
                    messages.success(request, f"Bienvenido, {user.nombre}")
                    return redirect('index')
                else:
                    messages.error(request, "Contraseña incorrecta")
            except Usuario.DoesNotExist:
                messages.error(request, "Usuario no encontrado")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form' : form})
