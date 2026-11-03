from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('novo/', views.PecaCreateView.as_view(), name='peca_create'),
    path('editar/<int:pk>/', views.PecaUpdateView.as_view(), name='peca_update'),
    path('excluir/<int:pk>/', views.PecaDeleteView.as_view(), name='peca_delete'),
]