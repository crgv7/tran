"""transporte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from transporte.view import autenticar,panel_secretaria
from .view import Vregistro, cerrar_sesion, ver_reserv


urlpatterns = [
    path('admin/', admin.site.urls),
#url de aplicaicones
    path('panel/', include('gestionreservacion.urls')),
    path('panels/panelv/', include('gestionvehiculo.urls')),
    path('panels/paneli/', include('gestionitinerario.urls')),
    path('panels/panelt/', include('gestiontarifa.urls')),
    path('panels/verreserv/', ver_reserv),
#-----------------------------------------------------------------------
    
    path("", autenticar),
    path('registrar/',Vregistro.as_view()),
    path("logout/", cerrar_sesion,name="cerrar_sesion"),
    path("panels/", panel_secretaria, name="panels"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )#carga los archivos media
