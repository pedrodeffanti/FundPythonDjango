from django.shortcuts import render
from funcionarios.forms import FuncionarioForms

def FuncionarioViews(request):
    if request.method == 'GET':
        form = FuncionarioForms()
        context = {
            'form': form
        }
        return render(request, 'funcionario.html', context=context)
    else:
        form = FuncionarioForms(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = FuncionarioForms

        context = {
            'form': form
        }
        return render(request, 'funcionarios.html')
