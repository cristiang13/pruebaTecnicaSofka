# Generated by Django 4.1.6 on 2023-02-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoLanzadera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_propulsion', models.CharField(max_length=100)),
                ('capacidad_transporte', models.FloatField()),
                ('peso', models.FloatField()),
                ('empuje', models.FloatField()),
                ('altura', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehiculoNoTripulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_propulsion', models.CharField(max_length=100)),
                ('capacidad_transporte', models.FloatField()),
                ('peso', models.FloatField()),
                ('empuje', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehiculoTripulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo_propulsion', models.CharField(max_length=100)),
                ('capacidad_transporte', models.FloatField()),
                ('peso', models.FloatField()),
                ('empuje', models.FloatField()),
                ('orbita', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
