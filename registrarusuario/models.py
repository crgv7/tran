from django.db import models

# Create your models here.

class registrar (models.Model): # tabla y campos de la base de datos
    nombre=models.CharField(max_length=15)
    correo=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    rpassword=models.CharField(max_length=20)





    def __str__(self):
        return self.name
