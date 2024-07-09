from django.urls import path
from . import views

urlpatterns = [
    path('comparar/', views.comparar_carreras, name='comparar_carreras'),
    path('carreras/', views.listar_carreras, name='lista_carreras'),
    path('agregar_a_comparacion/<int:carrera_id>/', views.agregar_a_comparacion, name='agregar_a_comparacion'),
    path('eliminar_de_comparacion/<int:carrera_id>/', views.eliminar_de_comparacion, name='eliminar_de_comparacion'),
    path('eliminar_todas_comparaciones/', views.eliminar_todas_comparaciones, name='eliminar_todas_comparaciones'),
    path('', views.home, name='home'),
]
