# Generated by Django 4.1 on 2022-09-05 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixs_dup', '0002_alter_detail_options_detailchangelog'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='备注'),
        ),
    ]
