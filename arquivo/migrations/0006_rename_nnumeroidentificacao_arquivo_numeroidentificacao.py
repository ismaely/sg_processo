# Generated by Django 3.2.4 on 2022-05-11 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arquivo', '0005_auto_20220511_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arquivo',
            old_name='nnumeroIdentificacao',
            new_name='numeroIdentificacao',
        ),
    ]