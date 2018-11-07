from django.db import models



# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    region = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    vivienda = models.CharField(max_length=50)
