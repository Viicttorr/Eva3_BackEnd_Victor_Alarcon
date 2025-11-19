from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('reservar_sala/<int:id>',views.reservar_sala,name="reservar_sala"),
    path('detalle_reserva/<int:id>',views.detalle_reserva,name="detalle_reserva"),
    path("api/last_update/", views.api_last_update, name="api_last_update"),
     
]