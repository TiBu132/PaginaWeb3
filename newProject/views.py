from django.shortcuts import render
from .models import Usuario, tipoUsuario
from .forms import UsuarioForm, tipoForm
# Create your views here.

def base(request):
    context={}
    return render(request,'base.html',context)

def inicio(request):
    usuarios = Usuario.objects.all()
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

def Inicio_sesion(request):
    context={}
    return render(request,'Inicio_sesion.html',context)

def crud(request):
    usuarios = Usuario.objects.all()
    context={"usuarios":usuarios}
    return render(request, 'user_list.html', context)

def crudTipo(request):
    tipos = tipoUsuario.objects.all()
    context = {"tipo": tipos}
    return render(request, "pages/tipo_list.html", context)


def userAdd(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["amaterno"]
        fechaNac = request.POST["fechaNac"]
        tipoUsuario = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apaterno=apaterno,
            amaterno=amaterno,
            fechaNac=fechaNac,
            tipoUsuario=objTipo,
            correo=correo,
            telefono=telefono,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        return render(request, "Usuario_add.html", context)


def userDel(request, pk):
    context = {}
    try:
        user = Usuario.objects.get(rut=pk)

        user.delete()
        usuarios = Usuario.objects.all()
        context = {"mensaje": "OK Registro eliminado", "usuario": usuarios}
        return render(request, "pages/user_list.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {"mensaje": "Error, Rut no encontrado...", "usuario": usuarios}
        return render(request, "pages/user_list.html", context)
    
def userEdit(request, pk):
    if pk != "":
        user = Usuario.objects.get(rut=pk)
        tipo = tipoUsuario.objects.all()
        context = {"usuario": user, "tipo": tipo}
        return render(request, "user_edit.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "user_list", context)

def addForm(request):
    form = UsuarioForm()
    context = {"form": form}
    return render(request, "addForm.html", context)

