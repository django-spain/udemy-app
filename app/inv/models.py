from django.db import models
from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text = 'Descripción de la categoría',
        unique=True
    )

    def __stf__(self):
        return '{}'.format(self.descripcion)

    # Ponemos en mayuscula al guardar
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self)


    class Meta:
        verbose_name_plural = "categorias"
