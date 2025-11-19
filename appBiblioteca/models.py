from django.db import models
from django.utils import timezone

class Salas(models.Model): 
    id_sala = models.AutoField(primary_key=True)
    nombre_sala = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id_sala)
    
    

class Reserva(models.Model): 
    id_reserva = models.AutoField(primary_key=True)
    rut_usuario = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateTimeField()
    id_sala = models.ForeignKey('Salas', on_delete=models.PROTECT)
    

    def __str__(self):
        return str(self.id_reserva)