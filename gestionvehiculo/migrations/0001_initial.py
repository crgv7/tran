# Generated by Django 4.1.2 on 2022-11-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricula', models.CharField(max_length=15)),
                ('Modelo', models.CharField(max_length=15)),
                ('vehiculo', models.CharField(choices=[('ligero', 'ligero'), ('guagua', 'guagua'), ('camion', 'camion')], default='camion', max_length=14)),
            ],
        ),
    ]
