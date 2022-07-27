from django.urls import path
from .views import FornecedorViews, PedidoViews

urlpatterns = [
    path('fornecedor/', FornecedorViews),
    path('compras/', PedidoViews),
]
