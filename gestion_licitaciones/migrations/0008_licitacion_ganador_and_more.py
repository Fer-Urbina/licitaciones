# Generated by Django 5.1.4 on 2024-12-17 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_licitaciones', '0007_remove_licitacion_ganador_and_more'),
        ('propuestas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='licitacion',
            name='ganador',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ganador_de', to='propuestas.propuesta'),
        ),
        migrations.AlterField(
            model_name='licitacion',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del equipo o dispositivo', max_length=255)),
                ('procesador', models.CharField(blank=True, max_length=255, null=True)),
                ('ram', models.CharField(blank=True, max_length=100, null=True)),
                ('almacenamiento', models.CharField(blank=True, max_length=100, null=True)),
                ('otros_detalles', models.TextField(blank=True, null=True)),
                ('licitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='gestion_licitaciones.licitacion')),
            ],
        ),
        migrations.DeleteModel(
            name='DetalleLicitacion',
        ),
    ]
