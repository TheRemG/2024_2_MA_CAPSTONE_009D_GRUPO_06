# Generated by Django 5.1.2 on 2024-12-09 23:41

import ventweb.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventweb', '0002_alter_usuario_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True, validators=[ventweb.models.validar_rut], verbose_name='Rut'),
        ),
    ]
