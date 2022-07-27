from django.contrib import admin

from .models import ClienteModels, ModeloModels

@admin.register(ClienteModels)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'email', 'tel', )

@admin.register(ModeloModels)
class AtividadeAdmin2(admin.ModelAdmin):
    list_display = ('nome', 'numero', 'material', 'reforma', 'fundir', 'matfund', 'quantFund', 'pesoFund', 'dataEnt',
                    'dataProd', 'dataFim', 'valor')
