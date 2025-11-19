from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Reserva


@receiver(post_save, sender=Reserva)
def actualizar_last_update(sender, instance, **kwargs):
    instance.last_update = timezone.now()
    instance.save(update_fields=["last_update"])