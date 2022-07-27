from django.shortcuts import render

def FuncionarioViews(request):
    return render(request, 'funcionarios.html')
