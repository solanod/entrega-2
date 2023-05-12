from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class FormularioContacto(forms.Form):
    
    nombre=forms.CharField(label="Nombre", required=True)    
    email=forms.CharField(label="Email", required=True)
    contenido=forms.CharField(label="Contenido", widget=forms.Textarea)
    
class emailform(forms.Form):
    nombre = forms.CharField(label='Nombre Completo', required=True, min_length=5, max_length=25, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Introduzca sus datos'}))
    email = forms.EmailField(label='Correo Electrónico', required=True, max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Introduzca su email'}))
    message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escriba aquí su mensaje...','rows':5}))