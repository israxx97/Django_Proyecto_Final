from .models import Vino, Bodega
from django.core.paginator import Paginator


def ctx_vinos(request):
    vinos = Vino.objects.all()
    paginator = Paginator(vinos, 3)

    page_number = request.GET.get('page')
    page_vinos = paginator.get_page(page_number)
    return {'page_vinos': page_vinos}


def ctx_vino(request):
    vino_id = request.GET.get('vino_id')
    vino = Vino.objects.raw(
        "SELECT id FROM core_vino WHERE id = {}".format(vino_id))
    return {'vino': vino}


def ctx_bodega(request):
    vino_id = request.GET.get('vino_id')
    query = "SELECT core_bodega.id, core_bodega.bodega, core_bodega.imagen FROM core_bodega INNER JOIN core_vino ON core_bodega.id = core_vino.bodega_id WHERE core_vino.id = {} LIMIT 1".format(
        vino_id)
    bodega = Vino.objects.raw(query)
    return {'bodega': bodega}
