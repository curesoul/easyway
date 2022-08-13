from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)


class SpecsProduct(models.Model):
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
    product = models.ManyToManyField(choices=Product)
    lot = models.IntegerField(verbose_name='Lot')


class MixSSpecs(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mv = models.FloatField(verbose_name='门尼')
    mv_min = models.FloatField(verbose_name='门尼最小值')
    mv_max = models.FloatField(verbose_name='门尼最大值')


class MixSCheckResult(models.Model):
    specs = models.ForeignKey(MixSSpecs, on_delete=models.CASCADE)


class MixSCheckDetail(models.Model):
    check_result = models.ForeignKey(MixSCheckResult, on_delete=models.CASCADE)
    batch = models.IntegerField(default=1)
    mv = models.FloatField(verbose_name='门尼值')


class MixA(models.Model):


class MixB(models.Model):
