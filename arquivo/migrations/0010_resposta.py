# Generated by Django 4.0.2 on 2022-05-20 15:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arquivo', '0009_arquivo_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='arquivo.topologia')),
                ('resposta', models.CharField(blank=True, max_length=2, null=True)),
                ('detalhe', models.CharField(blank=True, max_length=190, null=True)),
                ('dataEntrada', models.DateField(default=django.utils.timezone.now)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
