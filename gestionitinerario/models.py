from django.db import models

# Create your models here.


class Itinerario(models.Model):
    ruta=models.CharField(max_length=15)
    hora_llegada=models.IntegerField(max_length=15)
    minutos_llegada=models.IntegerField(max_length=15)
    hora_salida=models.IntegerField(max_length=15)
    minutos_salida=models.IntegerField(max_length=15)

# Create your models here.
