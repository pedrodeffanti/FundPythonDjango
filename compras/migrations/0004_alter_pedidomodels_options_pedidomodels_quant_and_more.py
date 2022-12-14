# Generated by Django 4.0.6 on 2022-07-26 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_pedidomodels'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidomodels',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AddField(
            model_name='pedidomodels',
            name='quant',
            field=models.PositiveIntegerField(default=1, verbose_name='Quantidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidomodels',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Valor'),
            preserve_default=False,
        ),
    ]
