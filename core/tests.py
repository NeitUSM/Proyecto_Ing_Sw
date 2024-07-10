from django.test import TestCase, Client
from django.urls import reverse
from .models import Carrera
from .forms import FiltroGratuidadForm

class ListarCarrerasViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('lista_carreras')

        self.carrera1 = Carrera.objects.create(
            NombreUniversidad='Universidad 1',
            NombreCarrera='Carrera 1',
            DescripcionCarrera='Descripción 1',
            SemestresCarrera=8,
            RegionCarrera=1,
            ComunaCarrera='Comuna 1',
            AreaEstudio='Ingeniería',
            Arancel=3000000,
            Matricula=100000,
            Gratuidad=True,
            Regimen='Diurno',
            link='http://www.universidad1.cl/carrera1'
        )
        self.carrera2 = Carrera.objects.create(
            NombreUniversidad='Universidad 2',
            NombreCarrera='Carrera 2',
            DescripcionCarrera='Descripción 2',
            SemestresCarrera=10,
            RegionCarrera=2,
            ComunaCarrera='Comuna 2',
            AreaEstudio='Salud',
            Arancel=4000000,
            Matricula=200000,
            Gratuidad=False,
            Regimen='Vespertino',
            link='http://www.universidad2.cl/carrera2'
        )

    def test_listar_carreras_con_filtro_region(self):
        # Hacer una solicitud GET con el filtro de región
        response = self.client.get(self.url, {'region': 1})

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['carreras'],
            [self.carrera1],
            ordered=False
        )

    def test_listar_carreras_con_filtro_gratuidad(self):
        # Hacer una solicitud GET con el filtro de gratuidad
        response = self.client.get(self.url, {'gratuidad': True})

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['carreras'],
            [self.carrera1],
            ordered=False
        )

    def test_listar_carreras_con_filtro_area_estudio(self):
        # Hacer una solicitud GET con el filtro de área de estudio
        response = self.client.get(self.url, {'areaestudio': 'Ingeniería'})

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['carreras'],
            [self.carrera1],
            ordered=False
        )

    def test_listar_carreras_sin_filtro(self):
        # Hacer una solicitud GET sin filtros
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['carreras'],
            [self.carrera1, self.carrera2],
            ordered=False
        )