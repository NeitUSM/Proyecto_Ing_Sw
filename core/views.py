from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrera
from django.http import JsonResponse
from .forms import FiltroGratuidadForm

def agregar_a_comparacion(request, carrera_id):
    # Verificar si la carrera con el ID especificado existe
    get_object_or_404(Carrera, IdCarrera=carrera_id)
    comparacion = request.session.get('comparacion', [])
    if len(comparacion) < 2 and carrera_id not in comparacion:
        comparacion.append(carrera_id)
        request.session['comparacion'] = comparacion
    return JsonResponse({'success': True, 'comparacion_count': len(comparacion)})

def eliminar_de_comparacion(request, carrera_id):
    comparacion = request.session.get('comparacion', [])
    if carrera_id in comparacion:
        comparacion.remove(carrera_id)
        request.session['comparacion'] = comparacion

    return redirect('comparar_carreras')

def eliminar_todas_comparaciones(request):
    request.session['comparacion'] = []
    return redirect('lista_carreras')

def comparar_carreras(request):
    comparacion_ids = request.session.get('comparacion', [])
    carreras = Carrera.objects.filter(IdCarrera__in=comparacion_ids)
    return render(request, 'core/comparar_carreras.html', {'carreras': carreras})

def home(request):
    return render(request,'core/home.html')

def listar_carreras(request):
    carreras = Carrera.objects.all()
    filtro_form = FiltroGratuidadForm(request.GET or None)
    mensaje_no_resultados = None
    cargado = False

    if filtro_form.is_valid():
        gratuidad = filtro_form.cleaned_data.get('gratuidad')
        areaestudio = filtro_form.cleaned_data.get('areaestudio')

        if gratuidad:
            carreras = carreras.filter(Gratuidad=True)
        if areaestudio:
            carreras = carreras.filter(AreaEstudio=areaestudio)
        
        if not carreras.exists():
            mensaje_no_resultados = "No se encontraron carreras con los filtros aplicados."
    else:
        cargado = True

    return render(request, 'core/lista_carreras.html', {
        'carreras': carreras,
        'filtro_form': filtro_form,
        'mensaje_no_resultados': mensaje_no_resultados,
        'cargado': cargado,
    })

def carrera_detail(request, carrera_id):
    carrera = get_object_or_404(Carrera, IdCarrera=carrera_id)
    return render(request, 'core/carrera_detail.html', {'carrera': carrera})
