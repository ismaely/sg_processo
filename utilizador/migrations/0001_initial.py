# Generated by Django 3.2.4 on 2022-05-13 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sigla', models.CharField(blank=True, default=' ', max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(blank=True, default=' ', max_length=90, null=True)),
                ('descricao', models.CharField(blank=True, default=' ', max_length=190, null=True)),
            ],
        ),
    ]