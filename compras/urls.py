from django.urls import path
from .views import FornecedorViews, PedidoViews, MaterialViews

urlpatterns = [
    path('fornecedor/', FornecedorViews),
    path('compras/', PedidoViews),
    path('material/', MaterialViews),
]
