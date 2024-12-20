# Generated by Django 5.1.4 on 2024-12-08 02:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('propuestas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.IntegerField()),
                ('comentarios', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('evaluador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluaciones_realizadas', to=settings.AUTH_USER_MODEL)),
                ('propuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluaciones', to='propuestas.propuesta')),
            ],
        ),
    ]
