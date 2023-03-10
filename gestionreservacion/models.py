from django.db import models
from django.contrib.auth.models import User
from gestionvehiculo.models import Vehiculo 

# Create your models here.

tipo=[
("carga","carga"),
("pasajero","pasajero"),
("mantenimiento","mantenimiento")
]

tipo_vehiculo=[
("ligero","ligero"),
("guagua","guagua"),
("camion","camion")
]

class Reservacion(models.Model):
    nombre=models.CharField(max_length=15)
    apellido=models.CharField(max_length=15)
    telefono=models.CharField(max_length=8)
    fecha=models.DateField(auto_now=False, auto_now_add=False)
    
    tipo=models.CharField(max_length=14,choices=tipo, default="carga")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo=models.OneToOneField(Vehiculo, on_delete=models.CASCADE, null=False, blank=False)
    
