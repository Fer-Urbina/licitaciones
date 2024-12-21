# Generated by Django 5.1.4 on 2024-12-17 03:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_licitaciones', '0003_licitacion_estado_alter_licitacion_usuario'),
        ('propuestas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='licitacion',
            name='estado',
            field=models.CharField(choices=[('Abierta', 'Abierta'), ('Cerrada', 'Cerrada')], default='Abierta', max_length=10),
        ),
        migrations.AlterField(
            model_name='licitacion',
            name='ganador',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='propuesta_ganadora', to='propuestas.propuesta'),
        ),
        migrations.AlterField(
            model_name='licitacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DetalleLicitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.CharField(help_text='Nombre del equipo o dispositivo', max_length=100)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('especificaciones', models.TextField(blank=True, help_text='Especificaciones o detalles adicionales')),
                ('licitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='gestion_licitaciones.licitacion')),
            ],
        ),
    ]
