from django.shortcuts import render
from .models import Usuario, tipoUsuario
# Create your views here.

def base(request):
    context={}
    return render(request,'base.html',context)

def inicio(request):
    usuarios = Usuario.objects.raw('SELECT * FROM Usuario')
    print(usuarios)
    context={"usuarios":usuarios}
    return render(request,'Inicio.html',context)

def fleetwood_mac(request):
    context={}
    return render(request,'fleetwood_mac.html',context)

def supertramp_cotc(request):
    context={}
    return render(request,'supertramp_cotc.html',context)
def Carrito(request):
    context={}
    return render(request,'Carrito.html',context)
def Contacto(request):
    context={}
    return render(request,'Contacto.html',context)
def inicio_sesion(request):
    context={}
    return render(request,'inicio_sesion.html',context)

def Registrarse(request):
    context={}
    return render(request,'Registrarse.html',context)

