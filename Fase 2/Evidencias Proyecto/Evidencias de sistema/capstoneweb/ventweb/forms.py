from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re



"""
def validar_rut(value):

    rut_pattern = r"^(\d{1,2})\.(\d{3})\.(\d{3})-(\d{1,2})$"
    match = re.match(rut_pattern, value)
    
    if not match:
        raise ValidationError("Formato de RUT inválido. Debe ser XX.XXX.XXX-X")
    
    rut_sin_dv = value.replace(".", "").split("-")[0]
    digito_verificador = value.split("-")[1]
    
    # Validar el RUT con el dígito verificador
    if not verificar_rut(rut_sin_dv, digito_verificador):
        raise ValidationError("RUT inválido.")
    
    return value

def verificar_rut(rut_sin_dv, digito_verificador):
    suma = 0
    multiplicador = 2
    for digito in reversed(rut_sin_dv):
        suma += int(digito) * multiplicador
        multiplicador = 9 if multiplicador == 7 else multiplicador + 1
    
    resto = suma % 11
    digito_calculado = 11 - resto
    
    if digito_calculado == 10:
        digito_calculado = "K"
    elif digito_calculado == 11:
        digito_calculado = "0"
    
    return str(digito_calculado).upper == digito_verificador.upper()

# Formulario de registro
class RegistroForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    rut = forms.CharField(max_length=12, validators=[validar_rut, verificar_rut])
    password = forms.CharField(widget=forms.PasswordInput, min_length=6, label="Contraseña")

class Meta:
    model = User
    fields = ("username", "email", "rut", "password")"""