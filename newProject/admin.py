from django.contrib import admin
from .models import Usuario, tipoUsuario, Vinilo

# Register your models here.

admin.site.register(tipoUsuario)
admin.site.register(Usuario)
admin.site.register(Vinilo)
