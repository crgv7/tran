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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from transporte.view import autenticar
#from transporte.view import registrar_user
from transporte.view import panel
from transporte.view import add_reservacion,eliminar,editar, panel_secretaria, panel_vehiculo, add_vehiculo
from .view import Vregistro, cerrar_sesion


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", autenticar),
    #path("login/registrar/", registrar_user),
    path('registrar/',Vregistro.as_view()),
    path("panel/", panel),
#    path("login/panel/", panel),
    path("add_reservacion/", add_reservacion),
    path("registrar/panel/", panel),
    path("eliminar/<id>", eliminar),
    path("editar/<id>", editar),
    path("", cerrar_sesion,name="cerrar_sesion"),
    path("panels/", panel_secretaria),
    path("panels/panelv/", panel_vehiculo),
    path("add_vehiculo/", add_vehiculo),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
