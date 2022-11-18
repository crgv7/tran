from django.db import models
# Create your models here.
tipo_vehiculo=[
("ligero","ligero"),
("guagua","guagua"),
("camion","camion")
]

class Vehiculo(models.Model):
    Matricula=models.CharField(max_length=15)
    Modelo=models.CharField(max_length=15)
    vehiculo=models.CharField(max_length=14, choices=tipo_vehiculo, default="camion")
    
