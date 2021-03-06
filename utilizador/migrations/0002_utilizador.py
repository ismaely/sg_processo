# Generated by Django 3.2.4 on 2022-05-13 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilizador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='auth.user')),
                ('ndi', models.CharField(max_length=40)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('foto', models.ImageField(blank=True, default='user.jpg', null=True, upload_to='user/')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
