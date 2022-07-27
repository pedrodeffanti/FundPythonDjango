from django.contrib import admin

from .models import FornecedorModels, MaterialModels, PedidoModels

@admin.register(FornecedorModels)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipoMat', 'email', 'tel', )

@admin.register(MaterialModels)
class AtividadeAdmin2(admin.ModelAdmin):
    list_display = ('mat', 'nome')

@admin.register(PedidoModels)
class AtividadeAdmin2(admin.ModelAdmin):
    list_display = ('fornecedor', 'quant', 'valor')
