# Generated by Django 4.1.5 on 2023-01-29 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionreservacion', '0008_remove_reservacion_dia_remove_reservacion_mes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='fecha',
            field=models.DateField(),
        ),
    ]
