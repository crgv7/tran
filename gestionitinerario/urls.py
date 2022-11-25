from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gestionitinerario.views import panel_itinerario, add_itinerario, eliminar, editar



urlpatterns = [
    path("", panel_itinerario),
    path("paneli/add_itinerario/", add_itinerario),
#   path("panelv/add_vehiculo/", add_vehiculo),
    path("paneli/eliminar/<id>", eliminar),
    path("paneli/editar/<id>", editar),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
