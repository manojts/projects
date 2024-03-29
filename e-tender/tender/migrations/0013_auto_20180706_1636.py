# Generated by Django 2.0.6 on 2018-07-06 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tender', '0012_auto_20180706_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='c_user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='company_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bidding',
            name='c_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='company_id', to='tender.company'),
        ),
    ]
