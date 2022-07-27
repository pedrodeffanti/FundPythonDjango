from django.db import models

class FuncionarioModels(models.Model):
    CARGO_CHOICE = [
        (1, 'Modelador'),
        (2, 'Auxiliar de Modelador'),
        (3, 'Forneiro'),
        (4, 'Macheiro'),
        (5, 'Rebarbador'),
        (6, 'Ajudante'),
        (7, 'Operador de Máquina'),
        (8, 'Assistente RH'),
        (9, 'Assistente Adm'),
        (10, 'PCP'),
    ]

    nome = models.CharField('Nome', max_length=150)
    cargo = models.IntegerField('Cargo', choices=CARGO_CHOICE)
    CPF = models.CharField('CPF', max_length=11)
    email = models.EmailField('E-mail', max_length=100, blank=True, null=True)
    tel = models.CharField('Telefone', max_length=11)
    cidade = models.CharField('Cidade/Estado', max_length=100)
    rua = models.CharField('Rua - Número', max_length=150)
    conta = models.CharField('Número da Conta', max_length=10, blank=True, null=True)
    salario = models.PositiveIntegerField('Salário')

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'


