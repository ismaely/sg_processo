# Generated by Django 4.0.2 on 2022-05-23 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arquivo', '0011_remove_resposta_detalhe_resposta_msg_and_more'),
        ('utilizador', '0002_utilizador'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizador',
            name='departamentoDestino',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='arquivo.departamento'),
            preserve_default=False,
        ),
    ]