from django import forms
from .models import Tarifa






#formulario

class tarifaform(forms.ModelForm):
    cantidad_km=forms.IntegerField(initial=0,max_value=10000,min_value=0,disabled=False, required=False)
    cantidad_pasajeros=forms.IntegerField(initial=0,max_value=10000,min_value=0,disabled=False, required=False)
    cantidad_peso=forms.IntegerField(initial=0,max_value=10000,min_value=0,disabled=False, required=False)

    class Meta:
        model=Tarifa
        fields=[
            "tipo_reservacion",
            "modelo",
            "cantidad_km",
            "cantidad_pasajeros",
            "cantidad_peso",


        ]
        widgets={
            "tipo_reservacion": forms.Select(attrs={"class": "btn btn-secondary dropdown-toggle", "id":"tipo_reservacion"}),
            "modelo": forms.TextInput(attrs={"class": "form-input","Placeholder": "Modelo", "id":"modelo"}),
    






        }
