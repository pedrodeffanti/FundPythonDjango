from django.shortcuts import render

def ClienteViews(request):
    return render(request, 'cliente.html')

def ModeloViews(request):
    return render(request, 'compras.html')
