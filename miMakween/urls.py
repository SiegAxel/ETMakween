from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('servicio',ServicioViewset)


urlpatterns = [
    path('api/', include(router.urls)),
    path('',index,name='IND'),
    path('Galeria/',galeria,name='GALE'),
    path('AboutUs/',aboutUs,name='QUIEN'),
    path('Registrar/',formRegistro,name='REGIS'),
    path('Contacto/',contacto,name='CONT'),
    path('Login/',formLogin,name='LOGIN'),
    path('Detalle/<int:id>/',detalleTrabajo,name='DETA'),
    path('Search/',busquedaAvanzada,name='SEARCH'),
    path('adMain/<id>/',adminMain,name='ADMAIN'),
    path('adGaleria/<id>/',adminGaleria,name='ADGALE'),
    path('adTrabajo/<id>/',adminTrabajo,name='ADTRA'),
    path('Perfil/<str:id>/',perfilLogin,name='PERFIL'),
    path('Logout/',logout_user,name='LOGOUT'),
    path('Reserva/',reserva,name='RES'),
    path('Checkout/',checkout,name='CHK'),
    path('actualizar_item/',actualizarItem,name='actualizar_item'),
    path('procesar_orden/',procesarOrden,name='procesar_orden'),


]