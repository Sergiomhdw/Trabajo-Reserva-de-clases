from django.test import SimpleTestCase
from reserva.forms import Reserva

class TestForms(SimpleTestCase):

    def test_ReservaForm_valido_data(self):
        form = Reserva(data={
            'horainicio':'11:00:00Z',
            'horafinal':'13:30:00Z',
            'descripcion':'examen',
            'alumnos':35,
            'cursos':'3ESOA',
        })
        
        self.assertTrue(form.is_valid())


    def test_ReservaForm_noValido_data(self):
        form = Reserva(data={
            'horainicio':'11:00:00Z',
            'horafinal':'13:30:00Z',
            'descripcion':'',
            'alumnos':'',
            'cursos':'3ESOA',
        })
        
        self.assertFalse(form.is_valid())
    
    def test_expense_form_no_data(self):
        form = Reserva(data={})

        self.assertFalse(form.is_valid())