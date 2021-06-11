import django
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import ramas

class TestUrls(SimpleTestCase):

    def test_login_url_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, django.contrib.auth.views.LoginView)

    def test_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, django.contrib.auth.views.LogoutView)
    
    def test_ramas_url_resolved(self):
        url = reverse('ramas')
        self.assertEquals(resolve(url).func, ramas)