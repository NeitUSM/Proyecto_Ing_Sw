from django.shortcuts import render
from django.db.models import Q
from .models import Carrera
from .forms import FiltroGratuidadForm

def lista_carreras(request):
    carreras = Carrera.objects.all()
    filtro_form = FiltroGratuidadForm(request.GET)
    mensaje_no_resultados = None  # Variable para el mensaje

    if filtro_form.is_valid():
        gratuidad = filtro_form.cleaned_data.get('gratuidad')
        if gratuidad:
            carreras = carreras.filter(gratuidad=True)

        if not carreras.exists():  # Verificar si hay resultados
            mensaje_no_resultados = "No se encontraron carreras con lo requerido"

    return render(request, 'lista_carreras.html', {
        'carreras': carreras, 
        'filtro_form': filtro_form,
        'mensaje_no_resultados': mensaje_no_resultados  # Pasar el mensaje a la plantilla
    })
