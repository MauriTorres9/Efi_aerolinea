# Generated by Django 5.2.3 on 2025-06-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerolineas', '0002_alter_asiento_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('ADM', 'Administrador'), ('EMP', 'Empleado'), ('PAS', 'Pasajero')], max_length=50),
        ),
    ]
