from django.shortcuts import render

def FornecedorViews(request):
    return render(request, 'fornecedor.html')

def PedidoViews(request):
    return render(request, 'pedido.html')
