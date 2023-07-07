from django.shortcuts import redirect, render
from .models import Usuario, tipoUsuario, Vinilo
from .forms import UsuarioForm, tipoForm
from .Carrito import Carrito
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    context={}
    return render(request,'base.html',context)

def inicio(request):
    vinilos = Vinilo.objects.all()
    return render(request,'Tienda/Inicio.html',{'vinilos': vinilos})

def fleetwood_mac(request):
    context={}
    return render(request,'Tienda/fleetwood_mac.html',context)

def supertramp_cotc(request):
    context={}
    return render(request,'Tienda/supertramp_cotc.html',context)

def carrito(request):
    vinilos = Vinilo.objects.all()
    return render(request,'Tienda/Carrito.html',{'vinilos': vinilos})

def Contacto(request):
    context={}
    return render(request,'Tienda/Contacto.html',context)

# Crud

def crud(request):
    usuarios = Usuario.objects.all()
    context={"usuarios":usuarios}
    return render(request, 'Usuario/user_list.html', context)

def crudTipo(request):
    tipos = tipoUsuario.objects.all()
    context = {"tipo": tipos}
    return render(request, "tipo_list.html", context)

# Añadir Usuario
def userAdd(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "Usuario/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            fechaNacimiento=fecha,
            tipoUsuario=objTipo,
            correo=correo,
            telefono=telefono,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        return render(request, "Usuario/user_add.html", context)

# Eliminar Usuario

def userDel(request, pk):
    context = {}
    try:
        user = Usuario.objects.get(rut=pk)

        user.delete()
        usuarios = Usuario.objects.all()
        context = {"mensaje": "OK Registro eliminado", "usuario": usuarios}
        return render(request, "Usuario/user_list.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {"mensaje": "Error, Rut no encontrado...", "usuario": usuarios}
        return render(request, "Usuario/user_list.html", context)

# Modificar Usuario

def userEdit(request, pk):
    if pk != "":
        user = Usuario.objects.get(rut=pk)
        tipo = tipoUsuario.objects.all()
        context = {"usuario": user, "tipo": tipo}
        return render(request, "Usuario/user_edit.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "Usuario/user_list", context)
    
# Agregar Vinilo

def viniloAdd(request, Vinilo_id):
    carrito = Carrito(request)
    vinilo = Vinilo.objects.get(idVinilo=Vinilo_id)
    carrito.agregar(vinilo)
    return redirect("Inicio")

# Eliminar Vinilo

def viniloDel(request, vinilo_id):
    carrito = Carrito(request)
    vinilo = Vinilo.objects.get(id=vinilo_id)
    carrito.eliminar(vinilo)
    return redirect("Inicio")

# Restar Vinilo

def viniloRestar(request, vinilo_id):
    carrito = Carrito(request)
    vinilo = Vinilo.objects.get(id= vinilo_id)
    carrito.restar(vinilo)
    return redirect("Inicio")

# Limpiar Carrito

def carritoLimpiar (request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Inicio")


def formAdd(request):
    form = UsuarioForm()
    context = {"form": form}
    return render(request, "formAdd.html", context)

# Iniciar sesión

def login(request):
    context = {}
    if request.method != "POST":
        return render(request, "registration/login.html", context)
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        # print(f"Usuario: {username} \t Contraseña: {password}")
        # usuario = Usuario.objects.get(correo=username)
        if username == "jubadilla" and password == "contraseña1":
            request.session["nombreUsuario"] = username
            usuarios = Usuario.objects.all()
            context = {"usuario": usuarios}
            return render(request, "Usuario/user_list.html", context)
        else:
            context = {"mensaje": "Usuario y/o Contraseña erronea"}
            return render(request, "registration/login.html", context)

def logout(request):
    del request.session["nombreUsuario"]
    context = {"mensaje": "Usuario Desconectado"}
    return render(request, "registration/login.html", context)