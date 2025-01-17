# Generated by Django 5.0.1 on 2024-08-20 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('arma', '0001_initial'),
        ('servidor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cautela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datacautela', models.DateField(blank=True, null=True, verbose_name='DATA DA CAUTELA')),
                ('numerosgpe', models.CharField(blank=True, max_length=30, null=True, verbose_name='NUMERO SGPE')),
                ('responsavel', models.CharField(blank=True, max_length=140, null=True, verbose_name='RESPONSAVEL')),
                ('datadevolucao', models.DateField(blank=True, null=True, verbose_name='DATA DA DEVOLUÇÃO')),
                ('unidade', models.CharField(blank=True, max_length=140, null=True, verbose_name='UNIDADE')),
                ('matricula', models.CharField(blank=True, max_length=12, null=True, verbose_name='MATRÍCULA')),
                ('telefone', models.CharField(blank=True, max_length=18, null=True, verbose_name='TELEFONE')),
                ('numeropatri', models.CharField(blank=True, max_length=15, null=True, verbose_name='Nº PATRIMÔNIO')),
                ('numerosinarm', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nº SINARM')),
                ('especie', models.CharField(blank=True, max_length=50, null=True, verbose_name='ESPÉCIE')),
                ('modelo', models.CharField(blank=True, max_length=30, null=True, verbose_name='MODELO')),
                ('calibre', models.CharField(blank=True, max_length=30, null=True, verbose_name='CALIBRE')),
                ('observacao', models.CharField(blank=True, max_length=250, null=True, verbose_name='OBSERVAÇÃO')),
                ('marca', models.CharField(blank=True, max_length=80, null=True, verbose_name='MARCA')),
                ('capacidade', models.CharField(blank=True, max_length=10, null=True, verbose_name='CAPACIDADE')),
                ('qtcarregador', models.CharField(blank=True, max_length=25, null=True, verbose_name='CARREGADORES')),
                ('docregistro', models.CharField(blank=True, max_length=250, null=True, verbose_name='DOC DE REGISTRO')),
                ('tipo', models.CharField(blank=True, max_length=30, null=True, verbose_name='TIPO')),
                ('regional', models.CharField(blank=True, max_length=150, null=True, verbose_name='REGIONAL')),
                ('status', models.CharField(blank=True, max_length=15, null=True, verbose_name='STATUS')),
                ('acessorios', models.CharField(blank=True, max_length=250, null=True, verbose_name='ACESSÓRIOS')),
                ('numeroserie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='arma.arma')),
                ('servidor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servidor.servidor')),
            ],
        ),
    ]
