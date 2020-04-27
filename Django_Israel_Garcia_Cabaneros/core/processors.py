from .models import Vino
from django.core.paginator import Paginator

def ctx_vinos(request):
    vinos = Vino.objects.all()
    paginator = Paginator(vinos, 3)

    page_number = request.GET.get('page')
    page_vinos = paginator.get_page(page_number)
    return {'page_vinos': page_vinos}