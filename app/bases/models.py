from django.db import models
from django.contrib.auth.models import User

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    # Fecha de Creacion
    fc = models.DateTimeField(auto_now_add=True)
    # Fecha de Modificación
    fm = models.DateTimeField(auto_now=True)
    # Usuario que crea
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    # Usuario Modifica
    um = models.IntegerField(null=True, blank=True)


    # Decimos que es una clase abstracta para que Django no cree las migraciones
    class Meta:
        abstract=True