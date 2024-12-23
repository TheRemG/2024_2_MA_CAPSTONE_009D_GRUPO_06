from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, LoginForm, ImagenForm
from django.contrib import messages
from .models import Usuario, Imagen
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.db.models import Q  # Importar Q para consultas complejas

# Create your views here.

def index(request):

    search_query = request.GET.get('search', '')

    if search_query:
        imagenes = Imagen.objects.filter(titulo__icontains=search_query).order_by('-fecha_subida')
    else:
        imagenes = Imagen.objects.all().order_by('-fecha_subida')

        

    return render(request, 'index.html', {'imagenes': imagenes, 'search_query': search_query})

def preguntasfrecuentes(request):
    return render(request, 'preguntasfrecuentes.html')

def logon(request):
    if request.method == 'POST':
        usuario_form = ClienteForm(request.POST)
        if usuario_form.is_valid():
            # Guarda al usuario
            usuario = usuario_form.save(commit=False)
            usuario.set_password(usuario.password)  # Hashea la contraseña
            usuario.save()

            # Autentica e inicia sesión al usuario
            user = authenticate(request, username=usuario.rut, password=request.POST['password'])
            if user is not None:
                login(request, user)  # Inicia la sesión automáticamente
                messages.success(request, "Usuario registrado e iniciado sesión con éxito")
                return redirect('index')  # Redirige a la página principal
            else:
                messages.error(request, "Error al autenticar el usuario.")
        else:
            messages.error(request, "Por favor, corrige los errores del formulario.")
    else:
        usuario_form = ClienteForm()
    return render(request, 'logon.html', {'form': usuario_form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']

            # Autenticar usuario
            user = authenticate(request, username=rut, password=password)

            if user is not None:
                login(request, user)  # Iniciar sesión
                messages.success(request, f"Bienvenido, {user.nombre}")
                next_page = request.GET.get('next', 'index')
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
    return redirect('index')

@login_required
def subir_imagen(request):
    if request.method == 'POST':
        imgForm = ImagenForm(request.POST, request.FILES)
        if imgForm.is_valid():
            imagen = imgForm.save(commit=False)
            imagen.usuario = request.user
            imagen.save()
            return redirect('index')
    else:
        imgForm = ImagenForm()
    
    return render(request, 'subir_imagen.html', {'form' : imgForm})

@login_required
def eli_img(request, imagen_id):
    imagen = get_object_or_404(Imagen, id=imagen_id, usuario=request.user)

    if imagen.usuario == request.user:
        imagen.delete()
        
    return render(request, 'prod_usuario.html' )

@login_required
def prod_usuario(request):
    usuario_actual = request.user
    productos = Imagen.objects.filter(usuario=usuario_actual)

    return render(request, 'prod_usuario.html', {'imagen': productos})
