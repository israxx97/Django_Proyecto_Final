from django.db import models

# Create your models here.


class Social(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=20, help_text="Para que se muestre el icono usamos la página https://fontawesome.com/, deberemos poner como nombre 'fa fa-nombreredsocial' tal y como nos muestra la página web si accedemos al icono que queremos mostrar en nuestra web.")
    url = models.URLField(verbose_name="URL",
                          max_length=200, blank=True, null=True)
    created = models.DateField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateField(
        verbose_name="Fecha de última actualización", auto_now=True)

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Redes Sociales"
        ordering = [
            "created"
        ]

    def __str__(self):
        return self.nombre
