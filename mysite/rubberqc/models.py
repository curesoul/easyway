from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)


class ItemSpecs(models.Model):
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
    item = models.ManyToManyField(ItemSpecs)
    lot = models.IntegerField(verbose_name='Lot')


class MixSItemSpecs(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    mv = models.CharField(max_length=255, verbose_name='门尼')
    mv_min = models.FloatField(verbose_name='门尼最小值')
    mv_max = models.FloatField(verbose_name='门尼最大值')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '塑炼检查标准'


class MixSCheckResult(models.Model):
    item = models.ForeignKey(MixSItemSpecs, on_delete=models.CASCADE, verbose_name='品名')
    lot = models.IntegerField(verbose_name='Lot')

    def __str__(self):
        return str(self.lot)

    class Meta:
        verbose_name = verbose_name_plural = '塑炼成绩表'


class MixSCheckDetail(models.Model):
    check_result = models.ForeignKey(MixSCheckResult, on_delete=models.CASCADE)
    batch = models.IntegerField(default=1)
    mv = models.FloatField(verbose_name='门尼值')

    def __str__(self):
        return str(self.batch)

    class Meta:
        verbose_name = verbose_name_plural = '检查详情'

# class MixA(models.Model):


# class MixB(models.Model):
