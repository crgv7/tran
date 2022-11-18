from django import forms
from .models import Vehiculo






#formulario

class vehiculoform(forms.ModelForm):
   # repeat_password=forms.CharField(widget=forms.TextInput(attrs={"class": "form-input","Placeholder": "Repetir contraseña", "id":"rpassword", "name":"rpassword"}))


    class Meta:
        model=Vehiculo
        fields=[
            "Matricula",
            "Modelo",
            "vehiculo"


        ]
        widgets={
            "Matricula": forms.TextInput(attrs={"class": "form-input", "id":"name"}),
            "Modelo": forms.TextInput(attrs={"class": "form-input","Placeholder": "Modelo", "id":"correo"}),
            #"dia": forms.NumberInput(attrs={"class": "","Placeholder": "1", "id":"rpasswd", "max_value":"31", "initial":"19"}),
            "vehiculo": forms.Select(attrs={"class": "btn btn-secondary dropdown-toggle d-flex w-100 ps-4 pe-4","Placeholder": "vehiculo", "id":"rpassword"}),


        }
