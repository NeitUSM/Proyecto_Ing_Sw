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
            'AreaEstudio',
            'Arancel',
            'Matricula',
            'Gratuidad',
            'Regimen', 
            'link'

        ]

class FiltroGratuidadForm(forms.Form):
    gratuidad = forms.BooleanField(label='Gratuidad', required=False)
    areaestudio_choices = [("", "Seleccione una opción")] + [(area, area) for area in Carrera.objects.values_list('AreaEstudio', flat=True).distinct()]
    areaestudio = forms.ChoiceField(choices=areaestudio_choices, required=False, label='Área Estudio')
    region_choices = [("", "Selecciones una opción")] + [(region, region) for region in Carrera.objects.values_list('RegionCarrera', flat=True).distinct()]
    region = forms.ChoiceField(choices=region_choices, required=False, label='Región')
