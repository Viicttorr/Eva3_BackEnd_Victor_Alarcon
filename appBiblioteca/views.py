from django.shortcuts import render, redirect
from .models import Salas, Reserva
from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse

def index(request):
    salas = Salas.objects.all()
    
    for sala in salas:
        reserva_activa = Reserva.objects.filter(
            id_sala=sala,
            fecha_inicio__lte=timezone.now(),
            fecha_termino__gte=timezone.now()
        ).first()

        sala.reserva_activa = reserva_activa

        if reserva_activa:
            sala.disponible = False
        else:
            sala.disponible = True
            sala.save()
    context = {}   
    context['salas']= salas
    
    return render(request, 'index.html', context)


def reservar_sala(request, id):
    if request.method == 'POST':

        usuario = request.POST.get('nombre')
        rut = request.POST.get('rut')

        sala = Salas.objects.get(id_sala=id)
        
        try:
            if sala and usuario and rut:
                        obj = Reserva.objects.create(
                            rut_usuario=rut,
                            nombre_usuario=usuario,
                            fecha_termino=timezone.now() + timedelta(hours=2),
                            id_sala = sala

                        )
                        sala.disponible = False
                        sala.save()
                        print("Datos guardados") 
                        return redirect('index')
                        
            else:
                    print("No se guardó: dato incorrecto")
        except Exception as e:
            print("Error al guardar la reserva:", e)

    return render(request,"reservar.html")


def detalle_reserva(request, id):
    context = {}
    sala = Salas.objects.get(id_sala=id)
    reserva_activa = Reserva.objects.filter(
        id_sala=sala,
        fecha_inicio__lte=timezone.now(),
        fecha_termino__gte=timezone.now()
    )
    context['sala']= sala
    context['reserva']= reserva_activa
    return render(request,"detalle_reserva.html",context)



def api_last_update(request):
    reserva = Reserva.objects.order_by("-fecha_termino").first()
    if reserva:
        expired = reserva.fecha_termino <= timezone.now()
        return JsonResponse({
            "fecha_termino": reserva.fecha_termino.isoformat(),
            "expired": expired
        })
    return JsonResponse({"fecha_termino": None, "expired": True})


