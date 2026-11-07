from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PecaDeRoupa

def pagina_inicial(request):
    todas_as_roupas = PecaDeRoupa.objects.all()
    return render(request, 'loja/lista_roupas.html', {'roupas': todas_as_roupas})

class PecaCreateView(LoginRequiredMixin, CreateView):
    model = PecaDeRoupa
    fields = ['nome', 'tamanho', 'preco', 'imagem', 'categoria', 'cores']
    success_url = reverse_lazy('home')

class PecaUpdateView(LoginRequiredMixin, UpdateView):
    model = PecaDeRoupa
    fields = ['nome', 'tamanho', 'preco', 'imagem', 'categoria', 'cores']
    success_url = reverse_lazy('home')

class PecaDeleteView(LoginRequiredMixin, DeleteView):
    model = PecaDeRoupa
    success_url = reverse_lazy('home')