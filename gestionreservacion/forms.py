from django import forms
from .models import Reservacion






#formulario

class reservacionform(forms.ModelForm):
   # repeat_password=forms.CharField(widget=forms.TextInput(attrs={"class": "form-input","Placeholder": "Repetir contraseña", "id":"rpassword", "name":"rpassword"}))
    dia=forms.IntegerField(initial=1,max_value=31,min_value=1,disabled=False)
    mes=forms.IntegerField(initial=1,max_value=12,min_value=1,disabled=False)

    class Meta:
        model=Reservacion
        fields=[
            "nombre",
            "apellido",
            "telefono",
            "dia",
            "mes",
            "tipo",
            "vehiculo",
            "costo"

        ]
        widgets={
            "nombre": forms.TextInput(attrs={"class": "form-input", "id":"name"}),
            "apellido": forms.TextInput(attrs={"class": "form-input","Placeholder": "Correo", "id":"correo"}),
            "telefono": forms.TextInput(attrs={"class": "form-input","Placeholder": "Contraseña", "id":"password"}),
            #"dia": forms.NumberInput(attrs={"class": "","Placeholder": "1", "id":"rpasswd", "max_value":"31", "initial":"19"}),
            "tipo": forms.Select(attrs={"class": "btn btn-secondary dropdown-toggle", "id":"passwd"}),
            "vehiculo": forms.Select(attrs={"class": "btn btn-secondary dropdown-toggle d-flex w-100 ps-4 pe-4","Placeholder": "Contraseña", "id":"rpassword"}),
            "costo": forms.TextInput(attrs={"class": "form-input w-50","Placeholder": "costo", "id":"rpassword"}),

        }
