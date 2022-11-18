from django import forms
from .models import registrar




#formulario

class Registrarform(forms.ModelForm):
   # repeat_password=forms.CharField(widget=forms.TextInput(attrs={"class": "form-input","Placeholder": "Repetir contraseña", "id":"rpassword", "name":"rpassword"}))

    class Meta:
        model=registrar
        fields=[
            "nombre",
            "correo",
            "password",
            "rpassword"


        ]
        widgets={
            "nombre": forms.TextInput(attrs={"class": "form-input","Placeholder": "Nombre", "id":"name"}),
            "correo": forms.TextInput(attrs={"class": "form-input","Placeholder": "Correo", "id":"correo"}),
            "password": forms.TextInput(attrs={"class": "form-input","Placeholder": "Contraseña", "id":"password"}),
            "rpassword": forms.TextInput(attrs={"class": "form-input","Placeholder": "Contraseña", "id":"rpassword"}),
        }
