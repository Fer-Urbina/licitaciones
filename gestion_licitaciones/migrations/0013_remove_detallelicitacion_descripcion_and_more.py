# Generated by Django 5.1.4 on 2024-12-19 03:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_licitaciones', '0012_delete_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallelicitacion',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='detallelicitacion',
            name='precio_unitario',
        ),
        migrations.RemoveField(
            model_name='licitacion',
            name='ganador',
        ),
        migrations.AlterField(
            model_name='detallelicitacion',
            name='nombre',
            field=models.CharField(help_text='Nombre del equipo, por ejemplo, CPU, Monitor.', max_length=255),
        ),
        migrations.CreateModel(
            name='ComponenteTecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especificacion', models.CharField(help_text="Especificación técnica, por ejemplo, 'Procesador Intel Core i7'.", max_length=255)),
                ('detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentes', to='gestion_licitaciones.detallelicitacion')),
            ],
        ),
    ]