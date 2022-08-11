from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    PRODUCT_TYPE = [
        (0, '塑炼'),
        (1, 'A炼'),
        (2, 'B炼'),
    ]
    ROTOR_TYPE = [
        (1, 'Ml'),
        (2, 'Ms'),
    ]
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    product_type = models.IntegerField(choices=PRODUCT_TYPE, verbose_name='类型')
    mv = models.FloatField(verbose_name='门尼')
    scorch = models.FloatField(verbose_name='焦烧')
    fmin = models.FloatField(verbose_name='Fmin')
    fmax = models.FloatField(verbose_name='Fmax')
    t10 = models.FloatField(verbose_name='T10')
    t90 = models.FloatField(verbose_name='T90')
    sg = models.FloatField(verbose_name='SG')
    hs = models.FloatField(verbose_name='HS')
    m_percent = models.FloatField(verbose_name='M')
    tb = models.FloatField(verbose_name='TB')
    eb = models.FloatField(verbose_name='EB')
    rotor = models.IntegerField(choices=ROTOR_TYPE, default=1, verbose_name='转子')


class PurchaseOrder(models.Model):
    lot = models.IntegerField(verbose_name='Lot')


class Mastication(models.Model):
    batch = models.IntegerField(default=1)
