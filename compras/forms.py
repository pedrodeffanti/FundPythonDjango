from django import forms

from compras.models import FornecedorModels, MaterialModels, PedidoModels

class FornecedorForms(forms.ModelForm):
    class Meta:
        model = FornecedorModels
        fields = '__all__'

class MaterialForms(forms.ModelForm):
    class Meta:
        model = MaterialModels
        fields = '__all__'

class PedidoForms(forms.ModelForm):
    class Meta:
        model = PedidoModels
        fields = '__all__'
