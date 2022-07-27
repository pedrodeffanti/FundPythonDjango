from django.urls import path
from .views import FuncionarioViews

urlpatterns = [
    path('funcionarios/', FuncionarioViews),
]
