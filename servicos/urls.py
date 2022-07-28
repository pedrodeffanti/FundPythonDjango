from django.urls import path
from .views import ClienteViews, ModeloViews, index

urlpatterns = [
    path('', index),
    path('cliente/', ClienteViews),
    path('modelo/', ModeloViews),
]
