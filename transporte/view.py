#from django.http import HttpResponse
from django.shortcuts import render, redirect  # metodo para simplificar el codigo y cargar las vistas

from django.template.loader import get_template # para cargar plantillas


from registrarusuario.models import registrar
from registrarusuario.forms import Registrarform


from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



user=""


class Vregistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request,"transporte/template/registrar/index.html", {"form":form})
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
            return render(request,"transporte/template/registrar/index.html", {"form":form})
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
    return render(request, "transporte/template/Login_v2/index.html",{"form":form})

def users():# funcion para pasar el usuario para el gestionreservacion
    global usuario
    user=usuario.username
    return user




#-----------------------------------------------------------------------------

def panel_secretaria(request):
    return render(request, "transporte/template/panel_secretaria/index.html")
