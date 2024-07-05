from django import forms
from .models import Carrera

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = [
            'NombreUniversidad', 
            'NombreCarrera', 
            'DescripcionCarrera', 
            'SemestresCarrera', 
            'RegionCarrera', 
            'ComunaCarrera', 
            'Regimen', 
            'link'
        ]