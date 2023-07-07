"""
URL configuration for PaginaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from newProject.views import viniloAdd, viniloDel, viniloRestar, carritoLimpiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newProject.urls')),
    path("agregar/ <int:Vinilo_id>", viniloAdd , name="Add"),
    path('eliminar/<int:Vinilo_id>/', viniloDel , name="Del"),
    path('restar/<int:Vinilo_id>/', viniloRestar , name="Sub"),
    path('limpiar/', carritoLimpiar , name="Cls"),
    path("accounts/", include("django.contrib.auth.urls")),
]
