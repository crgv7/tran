from django.db import models

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
    telefono=models.CharField(max_length=7)
    dia=models.IntegerField()
    mes=models.IntegerField()
    tipo=models.CharField(max_length=14,choices=tipo, default="carga")
    vehiculo=models.CharField(max_length=14, choices=tipo_vehiculo, default="camion")
    costo=models.IntegerField()
