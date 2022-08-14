# Generated by Django 4.0.6 on 2022-08-13 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSpecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product_type', models.IntegerField(choices=[(0, '塑炼'), (1, 'A炼'), (2, 'B炼')], verbose_name='类型')),
                ('mv', models.FloatField(verbose_name='门尼')),
                ('scorch', models.FloatField(verbose_name='焦烧')),
                ('fmin', models.FloatField(verbose_name='Fmin')),
                ('fmax', models.FloatField(verbose_name='Fmax')),
                ('t10', models.FloatField(verbose_name='T10')),
                ('t90', models.FloatField(verbose_name='T90')),
                ('sg', models.FloatField(verbose_name='SG')),
                ('hs', models.FloatField(verbose_name='HS')),
                ('m_percent', models.FloatField(verbose_name='M')),
                ('tb', models.FloatField(verbose_name='TB')),
                ('eb', models.FloatField(verbose_name='EB')),
                ('rotor', models.IntegerField(choices=[(1, 'Ml'), (2, 'Ms')], default=1, verbose_name='转子')),
            ],
        ),
        migrations.CreateModel(
            name='MixSItemSpecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mv', models.FloatField(verbose_name='门尼')),
                ('mv_min', models.FloatField(verbose_name='门尼最小值')),
                ('mv_max', models.FloatField(verbose_name='门尼最大值')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.IntegerField(verbose_name='Lot')),
                ('item', models.ManyToManyField(to='rubberqc.itemspecs')),
            ],
        ),
        migrations.CreateModel(
            name='MixSCheckResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.IntegerField(verbose_name='Lot')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rubberqc.mixsitemspecs')),
            ],
        ),
        migrations.CreateModel(
            name='MixSCheckDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField(default=1)),
                ('mv', models.FloatField(verbose_name='门尼值')),
                ('check_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rubberqc.mixscheckresult')),
            ],
        ),
    ]
