from django import forms
from .models import Tarifa






#formulario

class tarifaform(forms.ModelForm):
   # repeat_password=forms.CharField(widget=forms.TextInput(attrs={"class": "form-input","Placeholder": "Repetir contraseña", "id":"rpassword", "name":"rpassword"}))
   cantidad_km=forms.IntegerField(initial=1,max_value=10000,min_value=1,disabled=False)

   class Meta:
       model=Tarifa
       fields=[
            "tipo_reservacion",
            "modelo",
            "cantidad_km"


        ]
       widgets={
            "tipo_reservacion": forms.TextInput(attrs={"class": "form-input", "id":"name"}),
            "modelo": forms.TextInput(attrs={"class": "form-input","Placeholder": "Modelo", "id":"correo"}),




        }
