from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Tipo(models.Model):
    tipo = models.CharField(_("Tipo"), max_length=40,
                            help_text="Introduce un nuevo tipo de vino.")
    created = models.DateField(
        _("Fecha de creación"), auto_now_add=True, help_text="Este campo se introducirá automáticamente.")
    updated = models.DateField(
        _("Fecha de última actualización"), auto_now=True, help_text="Este campo se introducirá automáticamente.")

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = [
            "created"
        ]

    def __str__(self):
        return f"{self.tipo}"


class Bodega(models.Model):
    bodega = models.CharField(_("Bodega"),
                              max_length=70, help_text="Introduce una nueva bodega.")
    imagen = models.ImageField(
        _("Imagen"), upload_to="bodegas", blank=True, null=True, help_text="Introduce la imagen corporativa de la bodega.")
    created = models.DateField(
        _("Fecha de creación"), auto_now_add=True, help_text="Este campo se introducirá automáticamente.")
    updated = models.DateField(
        _("Fecha de última actualización"), auto_now=True, help_text="Este campo se introducirá automáticamente.")

    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"
        ordering = [
            "created"
        ]

    def __str__(self):
        return f"{self.bodega}"


class Vino(models.Model):
    nombre = models.CharField(
        _("Nombre"), max_length=50, help_text="Introduce un nombre.")

    YEARS = [(str(year), str(year))
             for year in range(1950, datetime.date.today().year + 1)]

    anyo = models.CharField(_("Año"), choices=YEARS,
                            max_length=4, help_text="Selecciona un año.")

    tipo = models.ForeignKey(Tipo, verbose_name=_(
        "Tipo"), on_delete=models.CASCADE, help_text="Selecciona un tipo.")
    denominacion = models.CharField(_("Denominación de Origen"),
                                    max_length=100, help_text="Lugar de procedencia del producto.")
    bodega = models.ForeignKey(Bodega, verbose_name=_(
        "Bodega"), on_delete=models.CASCADE, help_text="Selecciona una bodega.")
    volumen = models.PositiveIntegerField(
        _("Volumen (cL)"), help_text="Campo entero positivo.")
    stock = models.PositiveIntegerField(_("Stock"), validators=[
                                        MinValueValidator(0)], help_text="Campo entero positivo.")
    ventas_totales = models.PositiveIntegerField(
        _("Unidades vendidas"), default=0, editable=False, validators=[MinValueValidator(0)])
    descripcion = models.TextField(
        _("Descripción"), max_length=1000, help_text="Introduce una descripción del producto.")
    imagen = models.ImageField(
        _("Imagen"), upload_to="vinos", blank=True, null=True, help_text="Introduce una imagen del vino a mostrar.")
    precio = models.FloatField()
    created = models.DateField(
        _("Fecha de creación"), auto_now_add=True, help_text="Este campo se introducirá automáticamente.")
    updated = models.DateField(
        _("Fecha de última actualización"), auto_now=True, help_text="Este campo se introducirá automáticamente.")

    class Meta:
        verbose_name = "Vino"
        verbose_name_plural = "Vinos"
        ordering = [
            "stock"
        ]

    def __str__(self):
        return f"{self.nombre} ({self.anyo})"
