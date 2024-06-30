from django.shortcuts import render

from .models import Carrera
from .forms import FiltroGratuidadForm

def lista_carreras(request):
    carreras = Carrera.objects.all()
    filtro_form = FiltroGratuidadForm(request.GET)

    if filtro_form.is_valid():
        gratuidad = filtro_form.cleaned_data.get('gratuidad')
        if gratuidad:
            carreras = carreras.filter(gratuidad=True)

    return render(request, 'lista_carreras.html', {'carreras': carreras, 'filtro_form': filtro_form})
