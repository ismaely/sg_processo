# Generated by Django 4.0.2 on 2022-05-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivo', '0008_arquivo_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
