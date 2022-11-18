# Generated by Django 4.1.2 on 2022-11-05 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=7)),
                ('dia', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('tipo', models.CharField(choices=[('carga', 'carga'), ('pasajero', 'pasajero'), ('mantenimiento', 'mantenimiento')], default='carga', max_length=14)),
                ('vehiculo', models.CharField(choices=[('ligero', 'ligero'), ('guagua', 'guagua'), ('camion', 'camion')], default='camion', max_length=14)),
                ('costo', models.IntegerField()),
            ],
        ),
    ]
