from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()

    def __str__(self):
        return f'Curso {self.nombre}, Comision: {self.comision}'
    
class Jugador(models.Model):
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()
