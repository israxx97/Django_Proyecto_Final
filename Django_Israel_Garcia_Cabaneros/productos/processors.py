from core.models import Vino


def ctx_vinos_unidades_vendidas(request):
    vinos_mas_vendidos = Vino.objects.raw(
        "SELECT id, nombre FROM core_vino ORDER BY ventas_totales DESC LIMIT 5"
    )
    return {'vinos_mas_vendidos': vinos_mas_vendidos}
