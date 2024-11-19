from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.CharField(max_length=50, verbose_name='Email')
    password = models.CharField(max_length=50, verbose_name='Password')

    def __str__(self):
        return self.rut

class Imagen(models.Model):
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='static/img/')
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
