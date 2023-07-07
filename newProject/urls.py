from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base, name = 'base'),
    path('Inicio',views.inicio,name = 'Inicio'),
    path('Fleetwood-Mac-Rumours',views.fleetwood_mac,name = 'fleetwood_mac'),
    path('Supertramp-Crime-Of-The-Century',views.supertramp_cotc,name = 'supertramp'),
    path('Carrito',views.carrito, name = 'Carrito'),
    path('Contacto',views.Contacto, name = 'Contacto'),
    path("userAdd", views.userAdd, name="userAdd"),
    path("userDel/ <str:pk>", views.userDel, name="userDel"),
    path("userEdit/ <str:pk>", views.userEdit, name="userEdit"),
    path('crud', views.crud, name='crud'),
    path("crudTipo", views.crudTipo, name="crudTipo"),
    path("formAdd", views.formAdd, name="formAdd"),
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]