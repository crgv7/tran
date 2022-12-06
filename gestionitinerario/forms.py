from django import forms
from .models import Itinerario






#formulario

class itinerarioform(forms.ModelForm):
   # repeat_password=forms.CharField(widget=forms.TextInput(attrs={"class": "form-input","Placeholder": "Repetir contraseña", "id":"rpassword", "name":"rpassword"}))
      hora_llegada=forms.IntegerField(initial=0,max_value=23,min_value=0,disabled=False)
      minutos_llegada=forms.IntegerField(initial=0,max_value=59,min_value=0,disabled=False)
      hora_salida=forms.IntegerField(initial=0,max_value=23,min_value=0,disabled=False)
      minutos_salida=forms.IntegerField(initial=0,max_value=59,min_value=0,disabled=False)

      class Meta:
          model=Itinerario
          fields=[
                "ruta",
                "hora_llegada",
                "minutos_llegada",
                "hora_salida",
                "minutos_salida",]
          widgets={
                "ruta": forms.Select(attrs={"class": "btn btn-secondary dropdown-toggle", "id":"rutas"}),
            #"dia": forms.NumberInput(attrs={"class": "","Placeholder": "1", "id":"rpasswd", "max_value":"31", "initial":"19"}),



        }
