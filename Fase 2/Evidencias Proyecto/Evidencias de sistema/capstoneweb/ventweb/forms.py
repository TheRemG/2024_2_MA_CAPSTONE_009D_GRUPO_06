from django import forms
from .models import Usuario, Imagen
import re

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'email', 'password']
        labels = {
            'rut' : 'Rut',
            'nombre' : 'Nombre',
            'email' : 'Email',
            'password' : 'Password',
        }
        widgets = {
            'rut' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su rut',
                    'id' : 'rut'
                }
            ),
            'nombre' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su nombre completo',
                    'id' : 'nombre'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su correo',
                    'id' : 'email'
                }
            ),
            'password' : forms.PasswordInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Ingrese su contraseña',
                    'id' : 'password'
                }
            )
        }
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        rut_pattern = r"^\d{1,2}\.\d{3}\.\d{3}-[0-9kK]$"
        if not re.match(rut_pattern,rut):   
            raise forms.ValidationError("El formato del rut es invalido ej: 12.456.789-0")

        if not self.verificar_dv(rut):
            raise forms.ValidationError("El rut ingresado no es valido")
            
        return rut

    @staticmethod
    def verificar_dv(rut):
        rut_sin_dv, dv = rut.replace('.', '').split('-')
        dv = dv.upper()  

        suma = 0
        multiplicador = 2

        for digito in reversed(rut_sin_dv):
            suma += int(digito) * multiplicador
            multiplicador = 9 if multiplicador == 7 else multiplicador + 1

        resto = suma % 11
        dv_calculado = 11 - resto

        if dv_calculado == 10:
            dv_calculado = 'k'
        elif dv_calculado == 11:
            dv_calculado = '0'
        else:
            dv_calculado = str(dv_calculado)

        return dv == dv_calculado



class LoginForm(forms.Form):
    rut = forms.CharField(
        max_length=12,
        label='RUT',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su rut',
            }
        )
    )
    password = forms.CharField(
        max_length=32,
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su contraseña',
            }
        )
    )

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = [
            'titulo',
            'descripcion',
            'imagen']
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Titulo de la producto',
                }),
            'descripcion' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Descripcion del producto',
                }),
            'imagen' : forms.ClearableFileInput(
                attrs={
                    'class' : 'form-control',
                }),
            }