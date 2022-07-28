from django.shortcuts import render
from compras.forms import FornecedorForms, MaterialForms, PedidoForms

def FornecedorViews(request):
    if request.method == 'GET':
        form = FornecedorForms()
        context = {
            'form': form
        }
        return render(request, 'fornecedor.html', context=context)
    else:
        form = FornecedorForms(request.POST)
        if form.is_valid():
            fornecedor = form.save()
            form = FornecedorForms

        context = {
            'form': form
        }
        return render(request, 'fornecedor.html', context=context)

def PedidoViews(request):
    if request.method == 'GET':
        form = PedidoForms()
        context = {
            'form': form
        }
        return render(request, 'pedido.html', context=context)
    else:
        form = PedidoForms(request.POST)
        if form.is_valid():
            pedido = form.save()
            form = PedidoForms

        context = {
            'form': form
        }
        return render(request, 'pedido.html', context=context)


def MaterialViews(request):
    if request.method == 'GET':
        form = MaterialForms()
        context = {
            'form': form
        }
        return render(request, 'material.html', context=context)
    else:
        form = MaterialForms(request.POST)
        if form.is_valid():
            material = form.save()
            form = MaterialForms

        context = {
            'form': form
        }
        return render(request, 'material.html', context=context)
