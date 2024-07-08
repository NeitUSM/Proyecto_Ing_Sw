from django.db import models

class Carrera(models.Model):
    IdCarrera = models.AutoField(primary_key=True)
    NombreUniversidad = models.CharField(max_length=255)
    NombreCarrera = models.CharField(max_length=255)
    DescripcionCarrera = models.TextField()
    SemestresCarrera = models.PositiveIntegerField()
    RegionCarrera = models.PositiveIntegerField()
    ComunaCarrera = models.CharField(max_length=255)
    AreaEstudio = models.CharField(max_length=100)
    Arancel = models.PositiveIntegerField(default=0)  # Define un valor predeterminado
    Matricula = models.PositiveIntegerField(default=0)  # Define un valor predeterminado
    Gratuidad = models.CharField(max_length=2, default='NO')  # Define un valor predeterminado
    Regimen = models.CharField(max_length=50, default='Diurno')  # Define un valor predeterminado
    link = models.URLField(max_length=200, default='')  # Define un valor predeterminado
    
    def __str__(self):
        return f"{self.NombreCarrera} - {self.NombreUniversidad}"

class Comparacion(models.Model):
    carreras = models.ManyToManyField(Carrera)
