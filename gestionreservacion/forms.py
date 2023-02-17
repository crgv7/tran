from django import forms
from .models import Reservacion
import re






#formulario

class reservacionform(forms.ModelForm):
    fecha = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))

    class Meta:
        model=Reservacion
        fields=[
            "nombre",
            "apellido",
            "telefono",
            "fecha",
            "tipo",
            "vehiculo",
          

        ]
        widgets={
            "nombre": forms.TextInput(attrs={"class": "form-input", "Placeholder": "Nombre", "id":"Nombre"}),
            "apellido": forms.TextInput(attrs={"class": "form-input","Placeholder": "Apellidos", "id":"apellido"}),
            "telefono": forms.TextInput(attrs={"class": "form-input","Placeholder": "Telefono", "id":"telefono"}),
            #"dia": forms.NumberInput(attrs={"class": "","Placeholder": "1", "id":"rpasswd", "max_value":"31", "initial":"19"}),
            "tipo": forms.Select(attrs={"class": "btn btn-secondary dropdown-toggle", "id":"passwd"}),
            "vehiculo": forms.Select(attrs={"class": "btn btn-secondary dropdown-toggle d-flex w-100 ps-4 pe-4","Placeholder": "Contraseña", "id":"rpassword"}),
           

        }
        
        
  
        
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if re.search(r'[a-z A-Z \W]', telefono) is not None:
            raise forms.ValidationError("Este numero no es valido")
        
        if len(telefono)<7:
            raise forms.ValidationError("Este numero no es valido")
        
        if re.search(r'^59|^50|^55|^53', telefono) is None:    
            raise forms.ValidationError("Este numero no es valido")

         # TODO Validation
    
        return telefono 
        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        
        if re.search(r'\d', nombre) is not None:
             raise forms.ValidationError("Este nombre no es valido") 
        elif re.search(r'\s', nombre) is not None: 
            raise forms.ValidationError("Este nombre no es valido") 
            # end if
            
        
             # TODO Validation
        
        return nombre
           
       
