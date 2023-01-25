from django.db import models
# Create your models here.
tipo_vehiculo=[
("ligero","ligero"),
("guagua","guagua"),
("camion","camion")
]

class Vehiculo(models.Model):
    Matricula=models.CharField(max_length=7)
    Modelo=models.CharField(max_length=15)
    vehiculo=models.CharField(max_length=14, choices=tipo_vehiculo, default="camion")
    
    class Meta:
        verbose_name = 'Reservación'
        verbose_name_plural = 'Reservaciones'

    def __str__(self):
        return self.vehiculo + "  matricula: "+ self.Matricula
    
