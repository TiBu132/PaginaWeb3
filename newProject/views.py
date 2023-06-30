from django.shortcuts import render

# Create your views here.

def base(request):
    context={}
    return render(request,'base.html',context)

def inicio(request):
    context={}
    return render(request,'Inicio.html',context)

def fleetwood_mac(request):
    context={}
    return render(request,'fleetwood_mac.html',context)

def supertramp_cotc(request):
    context={}
    return render(request,'supertramp_cotc.html',context)