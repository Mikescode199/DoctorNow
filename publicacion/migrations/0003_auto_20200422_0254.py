# Generated by Django 3.0.5 on 2020-04-22 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0002_auto_20200422_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='etiqueta_fuente_url',
            field=models.URLField(blank=True, default='Opcional'),
        ),
    ]