# Generated by Django 4.0.6 on 2022-07-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_funcionariomodels_salario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionariomodels',
            name='salario',
            field=models.PositiveIntegerField(verbose_name='Salário'),
        ),
    ]