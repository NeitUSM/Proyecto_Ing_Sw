from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
urlpatterns = [
    path('comparar/', views.comparar_carreras, name='comparar_carreras'),
    path('carreras/', views.listar_carreras, name='lista_carreras'),
    path('agregar_a_comparacion/<int:carrera_id>/', views.agregar_a_comparacion, name='agregar_a_comparacion'),
    path('eliminar_de_comparacion/<int:carrera_id>/', views.eliminar_de_comparacion, name='eliminar_de_comparacion'),
    path('carrera/<int:carrera_id>/', views.carrera_detail, name='carrera_detail'),
    path('eliminar_todas_comparaciones/', views.eliminar_todas_comparaciones, name='eliminar_todas_comparaciones'),
    path('', views.home, name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)