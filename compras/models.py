from django.db import models


class FornecedorModels(models.Model):
    MATERIAL_CHOICE = [
        (1, 'Madeira/MDF/Compensado'),
        (2, 'Isopor'),
        (3, 'Fundição/Consumíveis'),
        (4, 'Escritório/Ferramenta/Consumíveis'),
    ]

    nome = models.CharField('Fornecedor', max_length=100)
    tipoMat = models.IntegerField(verbose_name='Tipo do Fornecedor', choices=MATERIAL_CHOICE)
    cnpj = models.CharField('CNPJ', max_length=14)
    email = models.EmailField('E-mail', max_length=100)
    tel = models.CharField('Telefone', max_length=11)
    cidade = models.CharField('Cidade/Estado', max_length=100)
    rua = models.CharField('Rua - Número', max_length=150)
    conta = models.CharField('Número da Conta', max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

class MaterialModels(models.Model):
    mat = models.CharField('Material', max_length=150)
    nome = models.ForeignKey(FornecedorModels, verbose_name='Fornecedor', on_delete=models.CASCADE)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.mat)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'

class PedidoModels(models.Model):
    fornecedor = models.ForeignKey(FornecedorModels, verbose_name='Fornecedor', on_delete=models.CASCADE)
    material = models.ManyToManyField(MaterialModels)
    quant = models.PositiveIntegerField('Quantidade')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.fornecedor)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
