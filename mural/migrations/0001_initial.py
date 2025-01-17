# Generated by Django 5.0.1 on 2024-08-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinatario', models.CharField(max_length=50, verbose_name='Destinatario')),
                ('mensagem', models.CharField(max_length=3000, verbose_name='Mensagem')),
                ('remetente', models.CharField(max_length=50, verbose_name='Remetente')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('imagem_mural', models.ImageField(blank=True, null=True, upload_to='mural/')),
                ('imagem2_mural', models.ImageField(blank=True, null=True, upload_to='mural/')),
                ('resposta', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Resposta')),
            ],
        ),
    ]
