# Generated by Django 3.0.5 on 2020-04-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='etiqueta_fuente_url',
            field=models.URLField(blank=True),
        ),
    ]
