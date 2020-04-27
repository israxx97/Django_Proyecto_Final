from django.contrib import admin
from .models import Tipo, Bodega, Vino

# Register your models here.


class TipoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Tipo, TipoAdmin)


class BodegaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Bodega, BodegaAdmin)


class VinoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Vino, VinoAdmin)
