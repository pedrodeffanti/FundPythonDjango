from django import forms
from funcionarios.models import FuncionarioModels

class FuncionarioForms(forms.ModelForm):
    class Meta:
        model = FuncionarioModels
        fields = '__all__'
