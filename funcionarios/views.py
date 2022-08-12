from django.contrib.auth.models import User
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
        return render(request, 'funcionario.html')

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')

def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e conformação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário Cadastrado com Sucesso'
        data['class'] = 'alert-sucess'
    return render(request, 'create.html', data)
