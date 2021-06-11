from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [ #AÑADO MIS URLs DE MIS VISTAS

    
    
    path('',views.aulas, name="aulas"),
    path('un_aula/<int:id>',views.un_aula, name="un_aula"),
    path('detallesreserva/',views.detallesreserva,name="detallesreserva"),
    # path('misreservas/<int:id>',views.misreservas,name="misreservas"),
    path('misreservas/',views.misreservas,name="misreservas"),
    path('detallemisreservas/',views.detallemisreservas,name="detallemisreservas"),
    path('detallemisreservas_inicio/',views.detallemisreservas_inicio,name="detallemisreservas_inicio"),
    path('eliminarreserva/',views.eliminarreserva,name="eliminarreserva"),
    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)