from django.contrib import admin

from .models import FuncionarioModels

@admin.register(FuncionarioModels)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'tel', )

