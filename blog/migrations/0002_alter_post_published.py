# Generated by Django 5.0.2 on 2024-02-27 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 4, 58, 40, 759133, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicacion'),
        ),
    ]