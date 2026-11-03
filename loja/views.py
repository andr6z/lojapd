from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import PecaDeRoupa

def pagina_inicial(request):
    todas_as_roupas = PecaDeRoupa.objects.all()
    return render(request, 'loja/lista_roupas.html', {'roupas': todas_as_roupas})
class PecaCreateView(CreateView):
    model = PecaDeRoupa
    fields = ['nome', 'tamanho', 'preco', 'categoria', 'cores']
    success_url = reverse_lazy('home') # Volta pra home após salvar
class PecaUpdateView(UpdateView):
    model = PecaDeRoupa
    fields = ['nome', 'tamanho', 'preco', 'categoria', 'cores']
    success_url = reverse_lazy('home')
class PecaDeleteView(DeleteView):
    model = PecaDeRoupa
    success_url = reverse_lazy('home')