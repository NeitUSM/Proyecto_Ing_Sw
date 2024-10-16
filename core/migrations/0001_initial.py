# Generated by Django 5.0.3 on 2024-07-04 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('IdCarrera', models.AutoField(primary_key=True, serialize=False)),
                ('NombreUniversidad', models.CharField(max_length=255)),
                ('NombreCarrera', models.CharField(max_length=255)),
                ('DescripcionCarrera', models.TextField()),
                ('SemestresCarrera', models.PositiveIntegerField()),
                ('RegionCarrera', models.PositiveIntegerField()),
                ('ComunaCarrera', models.CharField(max_length=255)),
                ('Regimen', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Comparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carreras', models.ManyToManyField(to='core.carrera')),
            ],
        ),
    ]
