# Generated by Django 3.0 on 2020-03-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
