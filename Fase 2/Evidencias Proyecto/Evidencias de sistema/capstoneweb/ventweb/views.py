from django.shortcuts import render, redirect
from .forms import ClienteForm, LoginForm, ImagenForm
from django.contrib import messages
from .models import Usuario, Imagen
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate

# Create your views here.

def index(request):
    imagenes = Imagen.objects.all().order_by('-fecha_subida')
    return render(request, 'index.html', {'imagenes' : imagenes})


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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']

            # Intentar autenticar al usuario
            user = authenticate(request, username=rut, password=password)
            if user is not None:
                # Si el usuario es válido, iniciar sesión
                login(request, user)

                # Redirigir a la página de destino o al índice
                next_page = request.GET.get('next') or 'index'
                return redirect(next_page)
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Formulario inválido")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return render(request, 'login')

def subir_imagen(request):
    if request.method == 'POST':
        imgForm = ImagenForm(request.POST, request.FILES)
        if imgForm.is_valid():
            imagen = imgForm.save(commit=False)
            #imagen.usuario = request.user
            imagen.save()
            return redirect('index')
    else:
        imgForm = ImagenForm()
    
    return render(request, 'subir_imagen.html', {'form' : imgForm})

