# Generated by Django 4.1 on 2022-09-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixs_dup', '0006_item_rotor_item_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionplan',
            name='created',
            field=models.DateField(auto_now=True, verbose_name='出表时间'),
        ),
    ]