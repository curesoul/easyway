from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    abbreviation = models.CharField(max_length=10, verbose_name='缩写')
    name = models.CharField(max_length=255, verbose_name='公司名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '客户'


# class Operator(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, blank=True, verbose_name='姓名')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = verbose_name_plural = '操作员'


class Item(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='客户')
    name = models.CharField(max_length=255, verbose_name='品名')
    mv = models.CharField(max_length=255, verbose_name='门尼')
    mv_min = models.FloatField(verbose_name='最小值')
    mv_max = models.FloatField(verbose_name='最大值')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '品名清单'


class Lot(models.Model):
    lot = models.IntegerField(verbose_name='批号')

    def __str__(self):
        return str(self.lot)

    class Meta:
        verbose_name = verbose_name_plural = '批号'


class Detail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, verbose_name='品名')
    lot = models.ForeignKey(Lot, on_delete=models.PROTECT, verbose_name='批号')
    batch = models.IntegerField(verbose_name='回数')
    mv = models.FloatField(verbose_name='门尼值')

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = verbose_name_plural = '检查成绩表'
