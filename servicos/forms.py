from django import forms
from servicos.models import ClienteModels, ModeloModels


class ClienteForms(forms.ModelForm):
    class Meta:
        model = ClienteModels
        fields = '__all__'

class ModeloForms(forms.ModelForm):
    class Meta:
        model = ModeloModels
        fields = '__all__'
