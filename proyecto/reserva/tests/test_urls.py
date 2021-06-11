import django
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reserva.views import aulas, un_aula, detallesreserva, misreservas, detallemisreservas, detallemisreservas_inicio, eliminarreserva

class TestUrls(SimpleTestCase):
    
    def test_aulas_url_resolved(self):
        url = reverse('aulas')
        self.assertEquals(resolve(url).func, aulas)

    def test_un_aula_url_resolved(self):
        url = reverse('un_aula', args=[6])
        self.assertEquals(resolve(url).func, un_aula)
    
    def test_detallesreserva_url_resolved(self):
        url = reverse('detallesreserva')
        self.assertEquals(resolve(url).func, detallesreserva)


    def test_misreservas_url_resolved(self):
        url = reverse('misreservas')
        self.assertEquals(resolve(url).func, misreservas)

    
    def test_detallemisreservas_url_resolved(self):
        url = reverse('detallemisreservas')
        self.assertEquals(resolve(url).func, detallemisreservas)


    def test_detallemisreservas_inicio_url_resolved(self):
        url = reverse('detallemisreservas_inicio')
        self.assertEquals(resolve(url).func, detallemisreservas_inicio)


    def test_eliminarreserva_url_resolved(self):
        url = reverse('eliminarreserva')
        self.assertEquals(resolve(url).func, eliminarreserva)   