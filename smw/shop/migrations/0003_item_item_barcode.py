# Generated by Django 2.0.6 on 2018-10-04 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181003_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_barcode',
            field=models.IntegerField(default=None, unique=True),
        ),
    ]
