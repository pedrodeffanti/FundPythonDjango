from django.urls import path
from .views import ClienteViews, ModeloViews

urlpatterns = [
    path('cliente/', ClienteViews),
    path('servico/', ModeloViews),
]

