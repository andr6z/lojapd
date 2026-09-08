from django.shortcuts import render
from .models import PecaDeRoupa

def pagina_inicial(request):
    todas_as_roupas = PecaDeRoupa.objects.all()
    
    return render(request, 'loja/lista_roupas.html', {'roupas': todas_as_roupas})