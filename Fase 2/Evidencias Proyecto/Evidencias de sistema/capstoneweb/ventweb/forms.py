from django import forms
from .models import Usuario, Imagen

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

class ImagenForm(forms.ModelForm:
    class Meta:
        model = Imagen
        fields = [
            'titulo',
            'descripcion',
            'imagen'
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
        ]
    )