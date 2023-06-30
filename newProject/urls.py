from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base, name = 'base'),
    path('Inicio',views.inicio,name = 'Inicio'),
    path('Fleetwood-Mac-Rumours',views.fleetwood_mac,name = 'fleetwood_mac'),
    path('Supertramp-Crime-Of-The-Century',views.supertramp_cotc,name = 'supertramp')
]