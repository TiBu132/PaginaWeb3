from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base, name = 'base'),
    path('Inicio',views.inicio,name = 'Inicio'),
    path('Fleetwood-Mac-Rumours',views.fleetwood_mac,name = 'fleetwood_mac'),
    path('Supertramp-Crime-Of-The-Century',views.supertramp_cotc,name = 'supertramp'),
    path('Carrito',views.Carrito, name = 'Carrito'),
    path('Contacto',views.Contacto, name = 'Contacto'),
    path('Inicio_sesion',views.Inicio_sesion, name = 'Inicio_sesion'),
    path("user_add", views.user_add, name="user_add"),
    path("user_del/ <str:pk>", views.user_del, name="user_del"),
    path("user_edit/ <str:pk>", views.user_edit, name="user_edit"),
    path('crud', views.crud, name='crud'),
    path("add_form", views.add_form, name="add_form"),
]