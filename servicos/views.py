from django.shortcuts import render
from servicos.forms import ClienteForms, ModeloForms


def ClienteViews(request):
    if request.method == 'GET':
        form = ClienteForms()
        context = {
            'form': form
        }
        return render(request, 'cliente.html', context=context)
    else:
        form = ClienteForms(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ClienteForms

        context = {
            'form': form
        }
        return render(request, 'cliente.html', context=context)

def ModeloViews(request):
    if request.method == 'GET':
        form = ModeloForms
        context = {
            'form': form
        }
        return render(request, 'modelo.html', context=context)
    else:
        form = ModeloForms(request.POST)
        if form.is_valid():
            modelo = form.save()
            form = ModeloForms

        context = {
            'form': form
        }
        return render(request, 'modelo.html', context=context)
