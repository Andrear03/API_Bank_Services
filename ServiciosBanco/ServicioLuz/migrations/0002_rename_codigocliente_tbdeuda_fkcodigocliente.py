# Generated by Django 4.2 on 2023-04-29 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioLuz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbdeuda',
            old_name='CodigoCliente',
            new_name='FkCodigoCliente',
        ),
    ]
