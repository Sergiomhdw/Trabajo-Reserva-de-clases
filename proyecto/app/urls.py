from django.urls import path

from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [ #AÑADO MIS URLs DE MIS VISTAS
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ramas/',views.ramas, name="ramas"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)