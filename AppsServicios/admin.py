from django.contrib import admin

# Register your models here.

from AppsServicios.models import Servicios, Tecnologias, Contactos

admin.site.register(Servicios)
admin.site.register(Tecnologias)
admin.site.register(Contactos)