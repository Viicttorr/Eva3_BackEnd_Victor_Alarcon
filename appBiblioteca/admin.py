from django.contrib import admin
from .models import Salas, Reserva


@admin.register(Salas)
class SalasAdmin(admin.ModelAdmin):
    list_display = ['id_sala', 'nombre_sala', 'capacidad', 'disponible']
    list_display_links = ['nombre_sala']
    ordering = ['id_sala']


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id_reserva', 'rut_usuario', 'nombre_usuario', 'fecha_inicio', 'fecha_termino', 'id_sala']
    list_display_links = ['rut_usuario']
    list_editable = ('fecha_termino',)
    ordering = ['id_reserva']