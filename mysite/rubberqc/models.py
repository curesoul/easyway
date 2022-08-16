from django.db import models



class Mastication(models.Model):
    batch = models.IntegerField(default=1)