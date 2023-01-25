# Create your views here.
from django.shortcuts import render,redirect
from gestiontarifa.models import Tarifa
from gestiontarifa.forms import tarifaform
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def panel_tarifa(request):
        tarifass=Tarifa.objects.all().filter()
        return render(request, "gestiontarifa/template/panel_tarifa/panel.html", {"tarifass": tarifass})



@login_required
def add_tarifa(request):
    context={}

    if request.method == "POST":
        form=tarifaform(request.POST)
        print("entre al post")


        if form.is_valid():
            print("entre al if")                          # validacion del formula
            tipo_reservacion=form.cleaned_data.get("tipo_reservacion")

            modelo=form.cleaned_data.get("modelo")
            cantidad_km=form.cleaned_data.get("cantidad_km")
            cantidad_pasajeros=form.cleaned_data.get("cantidad_pasajeros")
            cantidad_peso=form.cleaned_data.get("cantidad_peso")


            reg=Tarifa.objects.create(
                tipo_reservacion=tipo_reservacion,
                modelo=modelo,
                cantidad_km=cantidad_km,
                cantidad_pasajeros=cantidad_pasajeros,
                cantidad_peso=cantidad_peso,
                costo=costo(cantidad_km)
            )
            reg.save()
# si no es post muestra el formulario

    form=tarifaform(initial={'cantidad_km': '0'})


    context["form"]=form
    return render(request, "gestiontarifa/template/panel_tarifa/add_tarifa.html",{"form":form})

@login_required
def eliminar(request, id):
    print("ente")
    tarifass=Tarifa.objects.all().filter()

    tarifass=Tarifa.objects.get(id=id)
    tarifass.delete()
    return redirect("/panels/panelt/")



@login_required
def editar(request, id):# me qude aqui en editar
    #    reservaciones=Reservacion.objects.all().filter(nombre=usuario)
    tarifass=Tarifa.objects.get(id=id)

    context={}
    form=tarifaform(initial={'tipo_reservacion': tarifass.tipo_reservacion,
                                      'modelo': tarifass.modelo,
                                      'cantidad_km': tarifass.cantidad_km
        })
    context["form"]=form

    if request.method == "POST":
        form=tarifaform(request.POST)

        if form.is_valid():                                  # validacion del formula
            tipo_reservacion=form.cleaned_data.get("tipo_reservacion")
            modelo=form.cleaned_data.get("modelo")
            cantidad_km=form.cleaned_data.get("cantidad_km")


            tarifass.tipo_reservacion=tipo_reservacion
            tarifass.modelo=modelo
            tarifass.cantidad_km=cantidad_km
            tarifass.costo=costo(cantidad_km)

            tarifass.save()
            return redirect('/panels/panelt/')

    return render(request, "gestiontarifa/template/panel_tarifa/editar_tarifa.html", context)

def costo(cantidad_km):
    costo=0
    costo=cantidad_km*100
    print("este es el costo:----->", costo)
    return costo
