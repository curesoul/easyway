# Generated by Django 4.1 on 2022-09-05 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixs_dup', '0004_detail_ship_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='ship_status',
        ),
        migrations.AddField(
            model_name='detail',
            name='shipment_status',
            field=models.BooleanField(default=False, verbose_name='出货状态'),
        ),
    ]
