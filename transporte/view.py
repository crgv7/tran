#from django.http import HttpResponse
from django.shortcuts import render, redirect  # metodo para simplificar el codigo y cargar las vistas

from django.template.loader import get_template # para cargar plantillas
from registrarusuario.models import registrar
from registrarusuario.forms import Registrarform
from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth import login




def autenticar (request):

    return render(request, "template/Login_v2/index.html")

def registrar_user(request):

    context={}
    if request.method == "POST":
        form=Registrarform(request.POST)
        if form.is_valid(): # validacion del formulario
            #conseguir los campos del formulario
            nombre=form.cleaned_data.get("nombre")
            correo=form.cleaned_data.get("correo")
            password=form.cleaned_data.get("password")
            rpassword=form.cleaned_data.get("rpassword")
            if password != rpassword: # si las contraseñas no coinciden muestra el error
                messages.error(request, "las contraseñas no coinciden")

            else: # si las contraseñas son correcta registra
                reg=registrar.objects.create(
                nombre=nombre,
                correo=correo,
                password=password,
                rpassword=rpassword,
                )
                reg.save()
                username=form.save()

                login(request, username) #no funciona esta linea ver porque
                return redirect("panel/")




    else: # si no es post muestra el formulario
        form=Registrarform()
    context["form"]=form

    return render(request,"template/registrar/index.html",context)

def panel(request):
    return render(request, "template/panel_reservacion/panel.html")

def add_reservacion(request):
        return render(request, "template/panel_reservacion/add_reservacion.html")
