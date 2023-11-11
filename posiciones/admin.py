from django.contrib import admin
from posiciones.models import Categoria, Competidor, Equipo, Carrera
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Competidor)
admin.site.register(Equipo)
admin.site.register(Carrera)