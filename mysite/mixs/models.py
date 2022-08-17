from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '客户'


class Operator(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = verbose_name_plural = '操作员'


class Item(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    mv = models.CharField(max_length=255, verbose_name='门尼')
    mv_min = models.FloatField(verbose_name='门尼最小值')
    mv_max = models.FloatField(verbose_name='门尼最大值')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '品名清单'


class Lot(models.Model):
    lot = models.IntegerField(verbose_name='批号')

    def __str__(self):
        return self.lot

    class Meta:
        verbose_name = verbose_name_plural = '批号'


class Detail(models.Model):
    Item = models.ForeignKey(Item, on_delete=models.PROTECT)
    lot = models.ForeignKey(Lot, on_delete=models.PROTECT)
    batch = models.IntegerField(verbose_name='回数')
    mv = models.FloatField(verbose_name='门尼值')

    def __str__(self):
        return str(self.batch)

    class Meta:
        verbose_name = verbose_name_plural = '检查成绩表'
