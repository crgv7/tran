# Generated by Django 4.1.5 on 2023-01-18 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionvehiculo', '0001_initial'),
        ('gestionreservacion', '0002_reservacion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionvehiculo.vehiculo'),
        ),
    ]
