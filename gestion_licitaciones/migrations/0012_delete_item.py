# Generated by Django 5.1.4 on 2024-12-18 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_licitaciones', '0011_detallelicitacion_precio_unitario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]