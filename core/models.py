from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=200)  # Nombre de la carrera (string)
    universidad = models.CharField(max_length=200)  # Nombre de la universidad (string)
    gratuidad = models.BooleanField(default=False)  # Si la carrera es gratuita (booleano)

    def __str__(self):
        return self.nombre  # Representación en texto de la carrera
