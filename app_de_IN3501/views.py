from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'app_de_IN3501/inicio.html')

def contacto(request):
    return render(request, 'app_de_IN3501/contacto.html')

def haztupedido(request):
    return render(request, 'app_de_IN3501/haztupedido.html')

def productos(request):
    return render(request, 'app_de_IN3501/productos.html')

def quienessomos(request):
    return render(request, 'app_de_IN3501/quienessomos.html')

def resultado(request):
    dato_mail = request.POST['mail']
    dato_telefono = request.POST['telefono']
    dato_nombre = request.POST['nombre']
    dato_seccion = request.POST['seccion']
    dato_tipo = request.POST['TipoContacto']
    dato_opinion = request.POST['opinion']
    contexto = {"opinion": dato_opinion, "TipoContacto":dato_tipo, "seccion":dato_seccion, "nombre":dato_nombre, "mail":dato_mail, "telefono":dato_telefono }
    return render(request,'app_de_IN3501/resultado.html', contexto)
def donas(request):
    return render(request, 'app_de_IN3501/donas.html')

def rollitos(request):
    return render(request, 'app_de_IN3501/rollitos.html')

def alfajores(request):
    return render(request, 'app_de_IN3501/alfajores.html')

def confirmacionpedido(request):
    dato_nombre = request.GET['nombre_name']
    dato_duda = request.GET['duda']
    dato_signo = request.GET['signo']
    dato_sangre = request.GET['duda2']
    dato_pedido = request.GET[ 'pedido']
    dato_email = request.GET[ 'email']
    dato_gen = request.GET[ 'seccion']
    contexto = {"seccion":dato_gen, "nombre_name":dato_nombre, "duda":dato_duda, 'signo':dato_signo, 'duda2':dato_sangre, 'pedido':dato_pedido, 'email':dato_email}

    return render(request, 'app_de_IN3501/confirmacionpedido.html', contexto)