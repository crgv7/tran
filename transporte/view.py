#from django.http import HttpResponse
from django.shortcuts import render, redirect  # metodo para simplificar el codigo y cargar las vistas

from django.template.loader import get_template # para cargar plantillas
from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from gestionvehiculo.models import Vehiculo
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType



user=""


class Vregistro(View):
    def get(self, request):
    
        form=UserCreationForm()
        return render(request,"transporte/template/registrar/index.html", {"form":form})
    def post(self, request):
        print("hizo post")
        global usuario
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            group=Group.objects.get(
                name="clientes"
            )
            usuario.groups.add(group)
            
            
            
            return redirect("/panel/")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,"transporte/template/registrar/index.html", {"form":form})
def cerrar_sesion(request):
    logout(request)
    return redirect("/")

def autenticar (request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_user=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            global usuario
            usuario=authenticate(username=nombre_user, password=contra)
            if usuario is not None:
                if usuario.username == 'secre': # aqui defino el rol de secretaria, si el usario es secre.
                    login(request, usuario) #logea a secre
                    return redirect("panels/") # y la redirecciona al panel de secretaria
                login(request, usuario)
                return redirect("panel/")
            else:
                messages.error(request, "usaurio no valido")
        else:
            messages.error(request,"informacion incorrecta")

    form=AuthenticationForm()
    return render(request, "transporte/template/Login_v2/index.html",{"form":form})


#-----------------------------------------------------------------------------
@login_required
def panel_secretaria(request):
    return render(request, "transporte/template/panel_secretaria/index.html")
