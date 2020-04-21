from django import forms 
from . import views
from .models import Usuario
from publicacion.models import Publicacion
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    #Con estas lineas de código podemos registrar a un usuario
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())



class NewUser(UserCreationForm):
    correo = forms.CharField(max_length=20)


class NewPublicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = [
            'etiqueta_tema',
            'etiqueta_contenido',
            'etiqueta_fuente_url',
        ]
        labels = {
            'etiqueta_tema': 'Tema',
            'etiqueta_contenido':'Descripcion',
            'etiqueta_fuente_url':'Agregar fuente (opcional)',
        }
        widgets = {
            'etiqueta_tema': forms.TextInput(attrs={'class':'barra_tema'}),
            'etiqueta_contenido': forms.TextInput(attrs={'class':'barra_descripcion'}),
            'etiqueta_fuente_url': forms.TextInput(attrs={'class':'barra_url'}),
        }





class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'usuario_nombre',
            'usuario_apellido_paterno',
            'usuario_apellido_materno',
            'usuario_ocupacion',
            'usuario_correo'
            ]

        labels = {
            'usuario_nombre' : 'Nombre',
            'usuario_apellido_paterno': 'Apellido Paterno',
            'usuario_apellido_materno': 'Apellido Materno',
            'usuario_ocupacion': 'Ocupacion ',
            'usuario_correo': 'Correo electronico'
        }

        widgets = {
            'usuario_nombre': forms.TextInput(attrs={'class':'form-input'}),
            'usuario_apellido_paterno' : forms.TextInput(attrs={'class':'form-input'}),
            'usuario_apellido_materno': forms.TextInput(attrs={'class':'form-input'}),
            'usuario_ocupacion': forms.TextInput(attrs={'class':'form-input'}),
            'usuario_correo': forms.TextInput(attrs={'class':'form-input'})
        }