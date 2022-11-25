from django.shortcuts import render,redirect
from gestionreservacion.models import Reservacion
from gestionreservacion.forms import reservacionform
from transporte.view import users
# Create your views here.

def panel(request):

    print("hola", users())
    reservaciones=Reservacion.objects.all().filter(nombre=users()) # para hacer filtro
    return render(request, "gestionreservacion/template/panel_reservacion/panel.html", {"reservaciones":reservaciones})

def add_reservacion(request):
        context={}

        if request.method == "POST":
            form=reservacionform(request.POST, initial={'nombre': users()})
            form.fields['nombre'].disabled = "False"




            if form.is_valid():                                  # validacion del formula
                nombre=form.cleaned_data.get("nombre")
                apellido=form.cleaned_data.get("apellido")
                telefono=form.cleaned_data.get("telefono")
                dia=form.cleaned_data.get("dia")
                mes=form.cleaned_data.get("mes")
                tipo=form.cleaned_data.get("tipo")
                vehiculo=form.cleaned_data.get("vehiculo")
                costo=form.cleaned_data.get("costo")

                reg=Reservacion.objects.create(
                    nombre=nombre,
                    apellido=apellido,
                    telefono=telefono,
                    dia=dia,
                    mes=mes,
                    tipo=tipo,
                    vehiculo=vehiculo,
                   costo=costo
                )
                reg.save()


# si no es post muestra el formulario

        form=reservacionform(initial={'nombre': users()} )
        form.fields['nombre'].disabled = "True"



        context["form"]=form
        return render(request, "gestionreservacion/template/panel_reservacion/add_reservacion.html", context)

def eliminar(request, id):
    print("llamo vista")
    reservaciones=Reservacion.objects.all().filter(nombre=users())
    reserv=Reservacion.objects.get(id=id)
    reserv.delete()
    return redirect("/panel/")

def editar(request, id):# me qude aqui en editar
#    reservaciones=Reservacion.objects.all().filter(nombre=usuario)
    reserv=Reservacion.objects.get(id=id)

    context={}
    form=reservacionform(initial={'nombre': reserv.nombre,
                                  'apellido': reserv.apellido,
                                  'telefono': reserv.telefono,
                                  'tipo': reserv.tipo,
                                  'dia': reserv.dia,
                                  'mes': reserv.mes,
                                  'vehiculo': reserv.vehiculo,
                                  'costo': reserv.costo})
    context["form"]=form

    if request.method == "POST":
        form=reservacionform(request.POST)

        if form.is_valid():                                  # validacion del formula
            nombre=form.cleaned_data.get("nombre")
            apellido=form.cleaned_data.get("apellido")
            telefono=form.cleaned_data.get("telefono")
            dia=form.cleaned_data.get("dia")
            mes=form.cleaned_data.get("mes")
            tipo=form.cleaned_data.get("tipo")
            vehiculo=form.cleaned_data.get("vehiculo")
            costo=form.cleaned_data.get("costo")

            reserv.nombre=nombre
            reserv.apellido=apellido
            reserv.telefono=telefono
            reserv.dia=dia
            reserv.mes=mes
            reserv.tipo=tipo
            reserv.vehiculo=vehiculo
            reserv.costo=costo
            reserv.save()
            return redirect('/panel/')

    return render(request, "gestionreservacion/template/panel_reservacion/editar_reservacion.html", context)
