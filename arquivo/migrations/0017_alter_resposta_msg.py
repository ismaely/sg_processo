# Generated by Django 4.0.2 on 2022-05-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivo', '0016_resposta_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='msg',
            field=models.CharField(blank=True, max_length=15990, null=True),
        ),
    ]
