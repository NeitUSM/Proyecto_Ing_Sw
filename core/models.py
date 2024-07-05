from django.db import models

# Create your models here.
class Carrera(models.Model):
    IdCarrera = models.AutoField(primary_key=True)
    NombreUniversidad = models.CharField(max_length=255)
    NombreCarrera = models.CharField(max_length=255)
    DescripcionCarrera = models.TextField()
    SemestresCarrera = models.PositiveIntegerField()
    RegionCarrera = models.PositiveIntegerField()
    ComunaCarrera = models.CharField(max_length=255)
    Regimen = models.CharField(max_length=50)
    link = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.NombreCarrera} - {self.NombreUniversidad}"

class Comparacion(models.Model):
    carreras = models.ManyToManyField(Carrera)