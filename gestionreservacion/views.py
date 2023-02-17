from django.shortcuts import render,redirect
from gestionreservacion.models import Reservacion   #importa el modelo del models.py
from gestionreservacion.forms import reservacionform # importa el formulario  del archivo form
from django.contrib.auth.decorators import login_required
from gestionvehiculo.models import Vehiculo
from django.contrib import messages
# Create your views here.

@login_required
def panel(request):

    reservaciones=Reservacion.objects.all().filter(user=request.user) # hace una consulta y hacer filtro por el nombre de usuario
                                                                   # selecciona todos los objetos de la tabla que coincida con el nombre del usuario y lo guarda
                                                                   # en esa variable



    return render(request, "gestionreservacion/template/panel_reservacion/panel.html", {"reservaciones":reservaciones}) # carga el html
                                                                                                                        # y sele pasa
                                                                                                                        #los objetos de la
                                                                                                                        # base de datos a la
@login_required                                                                                                                       # plantilla html
def add_reservacion(request):
        context={}
        form=reservacionform()
    
        if request.method == "POST":
            form=reservacionform(request.POST)
            print("hize post")
           
        #    form.vehiculo=vehiculo.get()
            print(form)
            if form.is_valid():                                  # validacion del formula
                nombre=form.cleaned_data.get("nombre")
                apellido=form.cleaned_data.get("apellido")
                telefono=form.cleaned_data.get("telefono")
                fecha=form.cleaned_data.get("fecha")
            
                tipo=form.cleaned_data.get("tipo")
                vehiculo=form.cleaned_data.get("vehiculo")
                costo=form.cleaned_data.get("costo")
                
                reg=Reservacion.objects.create( #crea objetos en la tabla
                    nombre=nombre,
                    apellido=apellido,
                    telefono=telefono,
                    fecha=fecha,
                    tipo=tipo,
                    vehiculo=vehiculo,
                   costo=costo,
                   user=request.user
                )
                reg.save()
               
                


# si no es post muestra el formulario

         #El nombre de usurio ya inicalizado en el campo
       

        context["form"]=form
        return render(request, "gestionreservacion/template/panel_reservacion/add_reservacion.html", context)
@login_required
def eliminar(request, id): # eliminar obejeto
    reservaciones=Reservacion.objects.all().filter(user=request.user)
    reserv=Reservacion.objects.get(id=id)
    reserv.delete()
    return redirect("/panel/")


@login_required
def editar(request, id): # editar reservacion

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
        f=form.fields['vehiculo']
        print(form.errors)
      
                                      # validacion del formula
        try:
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
            reserv.user=request.user
            reserv.full_clean()
            reserv.save()
            return redirect('/panel/')
        
        except Exception as e:
            print("no es posible")
            messages.error(request, "El vehiculo ya esta reservado")
   
       

    return render(request, "gestionreservacion/template/panel_reservacion/editar_reservacion.html", context)
