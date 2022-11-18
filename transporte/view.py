#from django.http import HttpResponse
from django.shortcuts import render, redirect  # metodo para simplificar el codigo y cargar las vistas

from django.template.loader import get_template # para cargar plantillas


from registrarusuario.models import registrar
from registrarusuario.forms import Registrarform

from gestionreservacion.models import Reservacion
from gestionreservacion.forms import reservacionform

from gestionvehiculo.models import Vehiculo
from gestionvehiculo.forms import vehiculoform



from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class Vregistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request,"template/registrar/index.html", {"form":form})
    def post(self, request):
        global usuario
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect("panel/")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,"template/registrar/index.html", {"form":form})
def cerrar_sesion(request):
    logout(request)
    return redirect("login/")










def autenticar (request):

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_user=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            global usuario
            usuario=authenticate(username=nombre_user, password=contra)
            if usuario is not None:
                 #me quede aqui para definir la secretaria
                if usuario.username == 'yo':
                    return redirect("panels/")
                login(request, usuario)
                return redirect("panel/")
            else:
                messages.error(request, "usaurio no valido")
        else:
            messages.error(request,"informacion incorrecta")

    form=AuthenticationForm()
    return render(request, "template/Login_v2/index.html",{"form":form})



def panel(request):
    global usuario

    reservaciones=Reservacion.objects.all().filter(nombre=usuario) # para hacer filtro
    return render(request, "template/panel_reservacion/panel.html", {"reservaciones":reservaciones})

def add_reservacion(request):
        context={}
        global usuario
        user=usuario
        if request.method == "POST":
            form=reservacionform(request.POST, initial={'nombre': user})
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

        form=reservacionform(initial={'nombre': user} )
        form.fields['nombre'].disabled = "True"



        context["form"]=form
        return render(request, "template/panel_reservacion/add_reservacion.html", context)

def eliminar(request, id):
    print("llamo vista")
    reservaciones=Reservacion.objects.all().filter(nombre=usuario)
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

    return render(request, "template/panel_reservacion/editar_reservacion.html", context)

def panel_secretaria(request):
    return render(request, "template/panel_secretaria/index.html")


def panel_vehiculo(request):
        vehiculoss=Vehiculo.objects.all().filter()
        return render(request, "template/panel_secretaria/panel_vehiculos/panel.html", {"vehiculoss": vehiculoss})




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
    return render(request, "template/panel_secretaria/panel_vehiculos/add_vehiculo.html",{"form":form})
