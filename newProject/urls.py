from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('base',views.base, name = 'base'),
    path('Inicio',views.inicio,name = 'Inicio'),
    path('fleetwood_mac',views.fleetwood_mac,name = 'Fleetwood-Mac-Rumours')
]