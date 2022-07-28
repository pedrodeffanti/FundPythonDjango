from django.db import models


class ClienteModels(models.Model):
    nome = models.CharField('Nome Fantasia', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=14)
    email = models.EmailField('E-mail', max_length=100)
    tel = models.CharField('Telefone', max_length=11)
    cidade = models.CharField('Cidade/Estado', max_length=100)
    rua = models.CharField('Rua - Número', max_length=150)
    conta = models.CharField('Número da Conta', max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class ModeloModels(models.Model):
    MATERIAL_CHOICE = [
        (1, 'Madeira'),
        (2, 'Compensado/MDF'),
        (3, 'Isopor'),
    ]
    FUNDICAO_CHOICE = [
        (1, 'Aluminio'),
        (2, 'Ferro'),
        (3, 'Aço'),
        (4, 'Aço Inox'),
        (5, 'Ferro Branco'),
    ]

    FUNDIR_CHOICE = [
        (1, 'Sim'),
        (2, 'Não'),
    ]
    REFORMA_CHOICE = [
        (1, 'Sim'),
        (2, 'Não'),
    ]

    nome = models.ForeignKey(ClienteModels, verbose_name='Cliente', on_delete=models.CASCADE)
    numero = models.CharField('Número do Modelo', max_length=20)
    material = models.IntegerField(verbose_name='Material do Modelo', choices=MATERIAL_CHOICE)
    reforma = models.IntegerField(verbose_name='Reformar Modelo?', choices=REFORMA_CHOICE)
    fundir = models.IntegerField(verbose_name='Peça para Fundir?', choices=FUNDIR_CHOICE)
    matfund = models.IntegerField(verbose_name='Material do Fundido', choices=FUNDICAO_CHOICE, blank=True, null=True)
    quantFund = models.IntegerField('Quatidade de Peças', blank=True, null=True)
    pesoFund = models.FloatField('Peso por Peça', blank=True, null=True)
    dataEnt = models.DateTimeField('Dia de Entrada do Serviço')
    dataProd = models.DateTimeField('Data do Início do Serviço')
    dataFim = models.DateTimeField('Data do Serviço Finalizado')
    valor = models.DecimalField('Valor do Serviço', max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
