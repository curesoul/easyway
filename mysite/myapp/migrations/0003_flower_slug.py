# Generated by Django 4.0.6 on 2022-07-30 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_flower_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
