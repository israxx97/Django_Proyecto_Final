from .models import Social

def ctx_dict(request):
    redes_sociales = Social.objects.all()
    return {'redes_sociales': redes_sociales}