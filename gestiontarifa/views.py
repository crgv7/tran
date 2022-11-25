# Create your views here.
from django.shortcuts import render,redirect
from gestiontarifa.models import Tarifa
from gestiontarifa.forms import tarifaform
# Create your views here.
def panel_tarifa(request):
        tarifass=Tarifa.objects.all().filter()
        return render(request, "gestiontarifa/template/panel_tarifa/panel.html", {"tarifass": tarifass})




def add_tarifa(request):
    context={}

    if request.method == "POST":
        form=tarifaform(request.POST)


        if form.is_valid():
            print("entre al if")                          # validacion del formula
            tipo_reservacion=form.cleaned_data.get("tipo_reservacion")

            modelo=form.cleaned_data.get("modelo")
            cantidad_km=form.cleaned_data.get("cantidad_km")


            reg=Tarifa.objects.create(
                tipo_reservacion=tipo_reservacion,
                modelo=modelo,
                cantidad_km=cantidad_km,
                costo=costo(cantidad_km)
            )
            reg.save()
# si no es post muestra el formulario

    form=tarifaform()
    context["form"]=form
    return render(request, "gestiontarifa/template/panel_tarifa/add_tarifa.html",{"form":form})


def eliminar(request, id):
    print("ente")
    tarifass=Tarifa.objects.all().filter()

    tarifass=Tarifa.objects.get(id=id)
    tarifass.delete()
    return redirect("/panels/panelt/")




def editar(request, id):# me qude aqui en editar
    #    reservaciones=Reservacion.objects.all().filter(nombre=usuario)
    tarifass=Tarifa.objects.get(id=id)

    context={}
    form=tarifaform(initial={'tipo_reservacion': vehi.tipo_reservacion,
                                      'modelo': vehi.modelo,
                                      'cantidad_km': vehi.cantidad_km
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
