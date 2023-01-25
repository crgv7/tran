from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from gestionitinerario.models import Itinerario
from gestionitinerario.forms import itinerarioform
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def panel_itinerario(request):
        itinerario=Itinerario.objects.all().filter()
        return render(request, "gestionitinerario/template/panel_itinerario/panel.html", {"itinerario": itinerario})


@login_required
def add_itinerario(request):
    context={}
    if request.method == "POST":
        form=itinerarioform(request.POST)
        if form.is_valid():                                   # validacion del formula
            ruta=form.cleaned_data.get("ruta")
            hora_llegada=form.cleaned_data.get("hora_llegada")
            minutos_llegada=form.cleaned_data.get("minutos_llegada")
            hora_salida=form.cleaned_data.get("hora_salida")
            minutos_salida=form.cleaned_data.get("minutos_salida")
            reg=Itinerario.objects.create(
                ruta=ruta,
                hora_llegada=hora_llegada,
                minutos_llegada=minutos_llegada,
                hora_salida=hora_salida,
                minutos_salida=minutos_salida,
            )
            reg.save()
# si no es post muestra el formulario
    form=itinerarioform()
    context["form"]=form
    return render(request, "gestionitinerario/template/panel_itinerario/add_itinerario.html",{"form":form})

@login_required
def eliminar(request, id):
    print("ente")
    itinerario=Itinerario.objects.all().filter()

    itinerario=Itinerario.objects.get(id=id)
    itinerario.delete()
    return redirect("/panels/paneli/")



@login_required
def editar(request, id):# me qude aqui en editar
    #    reservaciones=Reservacion.objects.all().filter(nombre=usuario)
    itinerario=Itinerario.objects.get(id=id)

    context={}
    form=itinerarioform(initial={'ruta': itinerario.ruta,
                                      'hora_llegada': itinerario.hora_llegada,
                                      'minutos_llegada': itinerario.minutos_llegada,
                                      'hora_salida': itinerario.hora_salida,
                                      'minutos_salida': itinerario.minutos_salida,
        })
    context["form"]=form

    if request.method == "POST":
        form=itinerarioform(request.POST)

        if form.is_valid():                                  # validacion del formula
            ruta=form.cleaned_data.get("ruta")
            hora_salida=form.cleaned_data.get("hora_salida")
            minutos_salida=form.cleaned_data.get("minutos_salida")
            hora_llegada=form.cleaned_data.get("hora_llegada")
            minutos_llegada=form.cleaned_data.get("minutos_llegada")



            itinerario.ruta=ruta
            itinerario.hora_salida=hora_salida
            itinerario.minutos_salida=minutos_salida
            itinerario.hora_llegada=hora_llegada
            itinerario.minutos_llegada=minutos_llegada


            itinerario.save()
            return redirect('/panels/paneli/')

    return render(request, "gestionitinerario/template/panel_itinerario/editar_itinerario.html", context)
