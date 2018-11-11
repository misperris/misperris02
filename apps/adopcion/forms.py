from django import forms
from apps.adopcion.models import Persona, Solicitud

class PersonaForm(forms.ModelForm):
    model = Persona
    fields = [  
        'nombre',
        'rut',
        'correo',
        'contrasena',
        'fecha_nacimiento',
        'region',
        'ciudad',
        'vivienda',
    ]
    labels = {
        'nombre': 'Nombre',
        'rut': 'Rut',
        'correo': 'Correo',
        'contrasena': 'Contraseña',
        'fecha_nacimiento': 'Fecha de nacimiento',
        'region': 'Region',
        'ciudad': 'Ciudad',
        'vivienda': 'Vivienda',
    }
    widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'rut': forms.TextInput(attrs={'class': 'form-control'}),
        'correo': forms.TextInput(attrs={'class': 'form-control'}),
        'contrasena': forms.TextInput(attrs={'class': 'form-control'}),
        'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
        'region': forms.TextInput(attrs={'class': 'form-control'}),
        'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
        'vivienda': forms.TextInput(attrs={'class': 'form-control'}),
    }

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'numero_mascotas',
            'razones',
        ]
        labels = {
            'numero_mascotas':'Numero de mascotas',
            'razones': 'Razones para adoptar',
        }
        widgets = {
            'numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
            'razones':forms.Textarea(attrs={'class':'form-control'}),
        }