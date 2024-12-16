from django.db import models

# Create your models here.
from django.db import models

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    tipo_combustible = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"
