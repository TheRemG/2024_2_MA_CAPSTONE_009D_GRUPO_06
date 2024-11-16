from django.shortcuts import render, redirect
from .forms import ClienteForm, LoginForm
from django.contrib import messages
from .models import Usuario, Imagen
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    imagenes = Imagen.objects.all().order_by('-fecha_subida')
    return render(request, 'index.html', {'imagenes' , imagenes})

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
    

@login_required
def subir_imagen(request):
    if request.method == 'POST':
        imgForm = ImagenForm(request.POST, request.FILES)
        if imgForm.is_valid():
            imagen = imgForm(commit=False)
            imagen.usuario = request.Usuario
            imagen.save()
            return redirect('index')
    else:
        imgForm = ImagenForm()
    
    return render(request, 'subImg.html', {'form' , imgForm})
