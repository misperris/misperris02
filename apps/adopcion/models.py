from django.db import models



# Create your models here.


class Persona(models.Model):
    nombre = models.TextField(max_length=50)
    rut = models.TextField(max_length=10)
    correo = models.EmailField()
    contrasena = models.TextField(max_length=10)
    fecha_nacimiento = models.DateField()
    region = models.TextField(max_length=50)
    ciudad = models.TextField(max_length=30)
    vivienda = models.TextField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete = models.CASCADE)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()