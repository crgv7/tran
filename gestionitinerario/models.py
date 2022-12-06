from django.db import models

# Create your models here.
rutas=[
("ruta1","ruta 1"),
("ruta2","ruta 2"),
("ruta3","ruta 3"),
("ruta4","ruta 4"),
("ruta5","ruta 5"),
("ruta6","ruta 6"),
("ruta7","ruta 7"),
("ruta8","ruta 8"),
("ruta9","ruta 9"),
]

class Itinerario(models.Model):
    ruta=models.CharField(max_length=15, choices=rutas, default="ruta1")
    hora_llegada=models.IntegerField(max_length=15)
    minutos_llegada=models.IntegerField(max_length=15)
    hora_salida=models.IntegerField(max_length=15)
    minutos_salida=models.IntegerField(max_length=15)

# Create your models here.
