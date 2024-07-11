from django.test import TestCase, Client
from django.urls import reverse
from django.http import Http404
from .models import Carrera

class CarreraDetailViewTest(TestCase):
    def setUp(self):
        self.carrera = Carrera.objects.create(IdCarrera=1, NombreCarrera='Ingeniería de Sistemas', SemestresCarrera=10, RegionCarrera= 13)

    def test_carrera_detail_view(self):
        client = Client()
        response = client.get(reverse('carrera_detail', args=[self.carrera.IdCarrera]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/carrera_detail.html')
        self.assertEqual(response.context['carrera'], self.carrera)

    def test_carrera_detail_view_not_found(self):
        client = Client()
        response = client.get(reverse('carrera_detail', args=[999]))
        self.assertEqual(response.status_code, 404)