# Generated by Django 2.0.6 on 2018-10-04 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procure_item',
            name='proc_item_weight',
        ),
    ]
