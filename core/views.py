from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrera
from django.http import JsonResponse

def listar_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'core/lista_carreras.html', {'carreras': carreras})

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
