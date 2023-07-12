from typing import Any, Optional
from django.db import models
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DetailView
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate,logout,login as login_auth
from django.core.files.base import ContentFile
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.utils.html import format_html
from django.contrib.auth.password_validation import password_validators_help_texts
from .models import *
from .Carrito import *
import datetime
import json
from rest_framework import generics, viewsets
from .serializer import ServicioSerializer




def password_validators_help_texts(password_validators=None):
    """
    Return a list of all help texts of all configured validators.
    """
    help_texts = []
    if password_validators is None:
        password_validators = get_default_password_validators()
    for validator in password_validators:
        help_texts.append(validator.get_help_text())
    return None

# Create your views here.
def formRegistro(request):
    if request.method == "POST":
        form = NuevoUsuario(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            Usuario.objects.create(user=user, foto=form.cleaned_data['foto'])
            
            messages.success(request,("Registro completado."))
            return redirect('LOGIN')
    else:
        form = NuevoUsuario()
    return render(request,"Registro.html", {'form':form})



def aboutUs(request):
    return render(request, "AcercaDeNosotros.html")


def adminGaleria(request,id):
    u=User.objects.get(username=id)
    usuario=Usuario.objects.get(user=u);
    t=Trabajos.objects.filter(mecanico=usuario)
    userid= User.objects.get(username=id)
    meccount= Usuario.objects.filter(is_mecanico=True).count()
    usercount= Usuario.objects.all().count()
    tcount= Trabajos.objects.all().count()
    contexto={'usuario':usuario,'userid':userid,'t':t,'meccount':meccount,'tcount':tcount,'usercount':usercount}
    return render(request, "AdminGaleria.html",contexto)


def adminMain(request,id):
    u=User.objects.get(username=id)
    usuario=Usuario.objects.get(user=u);
    t=Trabajos.objects.filter(mecanico=usuario)
    userid= User.objects.get(username=id)
    meccount= Usuario.objects.filter(is_mecanico=True).count()
    usercount= Usuario.objects.all().count()
    tcount= Trabajos.objects.all().count()
    contexto={'usuario':usuario,'userid':userid,'t':t,'meccount':meccount,'tcount':tcount,'usercount':usercount}
    return render(request, "AdminMain.html",contexto)

def adminTrabajo(request,id):
    u=User.objects.get(username=id)
    usuario=Usuario.objects.get(user=u);
    t=Trabajos.objects.filter(mecanico=usuario)
    categorias= Categoria.objects.all()
    usuarios= User.objects.all()

    #Contadores
    meccount= Usuario.objects.filter(is_mecanico=True).count()
    usercount= Usuario.objects.all().count()
    tcount= Trabajos.objects.all().count()
    contexto={'usuario':usuario,'t':t,'meccount':meccount,'tcount':tcount,'usercount':usercount,'categorias':categorias}
    aviso={'mensaje':''}
    if request.POST:
         nombre=request.POST.get("nombre")
         descripcion=request.POST.get("descripcion")
         foto=request.FILES.get("fotoForm")
         mecanico=request.POST.get("mecanico")
         mecanico_instance= Usuario.objects.get(user__username=mecanico)
         categoria=request.POST.get("categoria")
         categoria_instance= Categoria.objects.get(nombre=categoria)
         tr= Trabajos(titulo=nombre,descripcion=descripcion,foto=foto,mecanico=mecanico_instance,categoria=categoria_instance,)
         try:
             tr.save()
             aviso["mensaje"]="Trabajo añadido"
             galeria_instance = Galeria(foto=foto, trabajo=tr)
             galeria_instance.save()
             return redirect(reverse('ADTRA', args=[usuario.user.username]))
         except:
             aviso["mensaje"]="Error al añadir trabajo"
    return render(request, "AdminTrabajo.html",contexto)

def busquedaAvanzada(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        categoriaForm = request.POST.get('categoriaForm')
        mecanicoForm = request.POST.get('mecanicoForm')
        mecanico = Usuario.objects.filter(is_mecanico=True)
        categoria = Categoria.objects.all()
     
        print(searched)
        print(categoriaForm)
        print(mecanicoForm)
        if categoriaForm == 0 and mecanicoForm == 0:
            trabajos = Trabajos.objects.all()
            print(trabajos)
        elif searched == None and categoriaForm == 0 and mecanicoForm in mecanico:
            trabajos = Trabajos.objects.filter(mecanico__user__first_name__icontains=mecanicoForm) | Trabajos.objects.filter(mecanico__user__last_name__icontains=mecanicoForm)
            print(trabajos)

        else:
            trabajos = Trabajos.objects.filter(Q(titulo__icontains=searched)|Q(mecanico__user__first_name__icontains=searched)|Q(categoria__nombre__icontains=searched))

        return render(request, "BusquedaAvanzada.html",{'searched':searched,'trabajos':trabajos,'categoriaForm':categoriaForm,'mecanicoForm':mecanicoForm,'mecanico':mecanico,'categoria':categoria})
    else:
        return render(request, "BusquedaAvanzada.html",{})

def contacto(request):
    if request.POST:
        nombre=request.POST.get("formNombre")
        apellido=request.POST.get("formApellido")
        email=request.POST.get("formEmail")
        telefono=request.POST.get("formTelefono")
        mensaje=request.POST.get("formMensaje")
        cont= formulario_contacto(nombre=nombre, apellido=apellido, email=email, telefono=telefono, mensaje=mensaje)
        cont.save()
    return render(request, "Contacto.html")

def detalleTrabajo(request, id):
    trabajo= Trabajos.objects.get(idTrabajo=id)
    contexto= {"trabajo":trabajo}
    return render(request, "DetalleTrabajo.html",contexto)

def galeria(request):
    trabajo = Trabajos.objects.filter(publicar=True)
    cantidad= Trabajos.objects.filter(publicar=True).count()
    contexto={"trabajo":trabajo,'cantidad':cantidad}
    return render(request, "Galeria.html",contexto)

def index(request):
    mecanicos= Usuario.objects.filter(is_mecanico=True)
    usuario= Usuario.objects.filter(is_mecanico=True).order_by("pk").reverse()[:3]
    categorias = Categoria.objects.all()
    contexto={'categorias':categorias,'usuario':usuario,'mecanicos':mecanicos}
    trabajo = Trabajos.objects.filter(publicar=True).order_by("idTrabajo").reverse()[:3]
    contexto["trabajo"]=trabajo
    return render(request, "index.html",contexto)

def formLogin(request):
    usuario=User.objects.filter(username=User.username)
    contexto={'usuario':usuario,}
    if request.method == "POST":
        username = request.POST['formUser']
        password = request.POST['formContrasena']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login_auth(request, user)
            if Usuario().is_mecanico:
                return redirect(reverse('ADTRA', args=[usuario.user.username]))
            else:
                return redirect(reverse('PERFIL', args=[user.username]))
        else:
            messages.success(request,("Error de Login"))
            return redirect('LOGIN')
    else:
        return render(request, "Login.html",{})

def perfilLogin(request,id):
    print(f"aqui :{id}")
    u=User.objects.get(username=id)
    usuario=Usuario.objects.get(user=u);#filter(Usuario.username=id)
    t=Trabajos.objects.filter(mecanico=usuario)
    print(f"usuario : {usuario}")
    userid= User.objects.get(username=id)
    contexto={'usuario':usuario,'userid':userid,'t':t}
    return render(request, "PerfilLogin.html",contexto)


def logout_user(request):
    logout(request)
    messages.success(request,("Te has desconectado."))
    return redirect('IND')

def reserva(request):

    if request.user.is_authenticated:
        usuario = request.user.userprofile
        orden, created = Orden.objects.get_or_create(cliente=usuario, completado=False)
        items = orden.itemorden_set.all()
    else:
        items = []
        orden = {'get_total_carro':0,'get_items_carro':0}

    servicios = Servicio.objects.all()
    context = {'servicios':servicios,'items':items, 'orden':orden}  # Crear un diccionario de contexto con los datos que deseas pasar
    return render(request, "Reserva.html", context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def checkout(request):
   
    if request.user.is_authenticated:
        usuario = request.user.userprofile
        orden, created = Orden.objects.get_or_create(cliente=usuario, completado=False)
        items = orden.itemorden_set.all()
    else:
        items = []
        orden = {'get_total_carro':0,'get_items_carro':0}

    servicios = Servicio.objects.all()
    context = {'servicios':servicios,'items':items, 'orden':orden}  # Crear un diccionario de contexto con los datos que deseas pasar
    return render(request, "Checkout.html", context)


def actualizarItem(request):
    data = json.loads(request.body)
    servicioId = data.get('servicioId')
    action = data.get('action')

    print('Action:', action)
    print('servicioId', servicioId)

    usuario = request.user.userprofile
    servicio = Servicio.objects.get(id=servicioId)
    orden, created = Orden.objects.get_or_create(cliente=usuario, completado=False)

    itemOrden, created = ItemOrden.objects.get_or_create(orden=orden, servicio=servicio)

    if action == 'add':
        itemOrden.cantidad = (itemOrden.cantidad +1)
    elif action == 'remove':
        itemOrden.cantidad = (itemOrden.cantidad -1)

    itemOrden.save()

    if itemOrden.cantidad <= 0:
        itemOrden.delete()

    return JsonResponse('Se añadio un item', safe=False)

@csrf_exempt
def procesarOrden(request):
    transaccion_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        usuario = request.user.userprofile
        orden, created = Orden.objects.get_or_create(cliente=usuario, completado=False)
        total = data['form']['total']
        orden.transaccion_id = transaccion_id

        if total == orden.get_total_carro:
            orden.completado = True
        orden.save()
        

    else:
        print('Usuario no logeado.')

    print('Data:',request.body)
    return JsonResponse('Pago completado', safe=False)

class ServicioViewset(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    #queryset = Producto.objetcs
    serializer_class = ServicioSerializer
