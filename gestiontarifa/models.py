from django.db import models

# Create your models here.

class Tarifa(models.Model):
    tipo_reservacion=models.CharField(max_length=15)
    modelo=models.CharField(max_length=15)
    cantidad_km=models.IntegerField()
    costo=models.IntegerField()
