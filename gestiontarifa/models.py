from django.db import models

# Create your models here.

tipo_reservacion=[

("mantenimiento","mantenimiento"),
("pasaje","pasaje"),
("carga","carga"),

]


class Tarifa(models.Model):
    tipo_reservacion=models.CharField(max_length=15, choices=tipo_reservacion, default="mantenimiento")
    modelo=models.CharField(max_length=15)
    cantidad_km=models.IntegerField()
    costo=models.IntegerField()
