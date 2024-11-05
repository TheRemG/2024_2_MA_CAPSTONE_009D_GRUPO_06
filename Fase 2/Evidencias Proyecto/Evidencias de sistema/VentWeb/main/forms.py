from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    rut = forms.CharField(max_length=12, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "rut", "password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electronico ya esta en uso ")
        return email
    
    def clean_rut(self):
        rut = self.cleaned_data.get("rut")
        if User.objects.filter(rut=rut).exists():
            raise forms.ValidationError("El rut ingresado ya esta en uso")
        return rut
    
    def save(self, commit=True):
        user = super().save(commit)
        profile = Profile(user=user, rut=self.cleaned_data['rut'])
        if commit:
            profile.save()
        return user
