from django.urls import path
from .views import FuncionarioViews, create, store, home

urlpatterns = [
    path('funcionarios/', FuncionarioViews),
    path('', home),
    path('create/', create),
    path('store/', store),
]
