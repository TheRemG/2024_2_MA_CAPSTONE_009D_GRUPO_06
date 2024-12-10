from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
import re
from django.core.exceptions import ValidationError
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, rut, nombre, email, password=None):
        if not rut:
            raise ValueError("El usuario debe tener rut")
        usuario = self.model(
            rut=rut,
            nombre=nombre,
            email=self.normalize_email(email),
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, rut, nombre, email, password):
        usuario = self.create_user(
            rut=rut,
            nombre=nombre,
            email=email,
            password=password,
        )
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario

def validar_rut(rut):
    """ Valida si el RUT es correcto (sin puntos, con guion y dígito verificador) """
    # Eliminar puntos y guion
    rut = rut.replace(".", "").replace("-", "")
    
    # Verificar que el RUT contenga solo números y una letra (para el dígito verificador)
    if not re.match(r'^\d{7,8}[0-9kK]$', rut):
        raise ValidationError('El RUT debe tener entre 7 y 8 dígitos seguidos de un dígito verificador (ej: 12345678K).')
    
    # Separar el número del dígito verificador
    cuerpo = rut[:-1]
    dv = rut[-1].upper()

    # Calcular el dígito verificador
    suma = 0
    multiplicador = 2
    for numero in reversed(cuerpo):
        suma += int(numero) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    dv_calculado = 11 - (suma % 11)
    dv_calculado = '0' if dv_calculado == 11 else 'K' if dv_calculado == 10 else str(dv_calculado)
    
    # Verificar si el dígito verificador coincide
    if dv != dv_calculado:
        raise ValidationError(f'El RUT no es válido. Se esperaba el dígito verificador "{dv_calculado}".')

class Usuario(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name='Rut', unique=True, validators=[validar_rut])
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.CharField(max_length=50, verbose_name='Email')
    password = models.CharField(max_length=50, verbose_name='Password')
    is_active= models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['nombre', 'email']

    def __str__(self):
        return f'{self.nombre} - {self.rut}'

class Imagen(models.Model):
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='static/img/')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contactos = models.CharField(max_length=300, default="Sin contacto")
    fecha_subida = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
