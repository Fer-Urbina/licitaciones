# Generated by Django 5.1.4 on 2024-12-17 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_licitaciones', '0005_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallelicitacion',
            name='cantidad',
            field=models.PositiveIntegerField(default=1, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='detallelicitacion',
            name='especificaciones',
            field=models.TextField(blank=True, null=True, verbose_name='Especificaciones'),
        ),
        migrations.AlterField(
            model_name='detallelicitacion',
            name='nombre_equipo',
            field=models.CharField(max_length=255, verbose_name='Nombre del Equipo'),
        ),
    ]
