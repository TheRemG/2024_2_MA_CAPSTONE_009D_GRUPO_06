from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
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


class Usuario(AbstractBaseUser, PermissionsMixin):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name='Rut')
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
        return self.rut

class Imagen(models.Model):
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='static/img/')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
