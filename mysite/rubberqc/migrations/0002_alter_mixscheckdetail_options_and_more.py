# Generated by Django 4.0.6 on 2022-08-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubberqc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mixscheckdetail',
            options={'verbose_name': '检查详情', 'verbose_name_plural': '检查详情'},
        ),
        migrations.AlterModelOptions(
            name='mixscheckresult',
            options={'verbose_name': '塑炼成绩表', 'verbose_name_plural': '塑炼成绩表'},
        ),
        migrations.AlterModelOptions(
            name='mixsitemspecs',
            options={'verbose_name': '塑炼检查标准', 'verbose_name_plural': '塑炼检查标准'},
        ),
        migrations.AlterField(
            model_name='mixsitemspecs',
            name='mv',
            field=models.CharField(max_length=255, verbose_name='门尼'),
        ),
    ]