from django.shortcuts import render,redirect
from gestionvehiculo.models import Vehiculo
from gestionvehiculo.forms import vehiculoform
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def panel_vehiculo(request):
        vehiculoss=Vehiculo.objects.all().filter()
        return render(request, "gestionvehiculo/template/panel_vehiculos/panel.html", {"vehiculoss": vehiculoss})
@login_required
def add_vehiculo(request):
    context={}
    if request.method == "POST":
        form=vehiculoform(request.POST)
        if form.is_valid():
            print("entre al if")                          # validacion del formula
            Matricula=form.cleaned_data.get("Matricula")
            Modelo=form.cleaned_data.get("Modelo")
            vehiculo=form.cleaned_data.get("vehiculo")
            reg=Vehiculo.objects.create(
                Matricula=Matricula,
                Modelo=Modelo,
                vehiculo=vehiculo,
            )
            reg.save()
# si no es post muestra el formulario
    form=vehiculoform()
    context["form"]=form
    return render(request, "gestionvehiculo/template/panel_vehiculos/add_vehiculo.html",{"form":form})

@login_required
def eliminar(request, id):
    print("ente")
    vehiculoss=Vehiculo.objects.all().filter()
    vehi=Vehiculo.objects.get(id=id)
    vehi.delete()
    return redirect("/panels/panelv/")



@login_required
def editar(request, id):# me qude aqui en editar
    #    reservaciones=Reservacion.objects.all().filter(nombre=usuario)
    vehi=Vehiculo.objects.get(id=id)
    context={}
    form=vehiculoform(initial={'Matricula': vehi.Matricula,
                                      'Modelo': vehi.Modelo,
                                       'vehiculo': vehi.vehiculo
        })
    context["form"]=form

    if request.method == "POST":
        form=vehiculoform(request.POST)
        if form.is_valid():                                  # validacion del formula
            Matricula=form.cleaned_data.get("Matricula")
            Modelo=form.cleaned_data.get("Modelo")
            vehiculo=form.cleaned_data.get("vehiculo")
            #Actualizar datos
            vehi.Matricula=Matricula
            vehi.Modelo=Modelo
            vehi.vehiculo=vehiculo
            vehi.save()
            return redirect('/panels/panelv/')

    return render(request, "gestionvehiculo/template/panel_vehiculos/editar_vehiculo.html", context)
