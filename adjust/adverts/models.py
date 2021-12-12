from django.db import models
from model_utils import Choices


class PerformanceMeasure(models.Model):
    OS = Choices('ios', 'android')

    os = models.CharField(max_length=7, choices=OS, default=OS.android)
    date = models.DateField()
    clicks = models.PositiveIntegerField()
    installs = models.PositiveIntegerField()
    spend = models.DecimalField(max_digits=12, decimal_places=2,)
    revenue = models.DecimalField(max_digits=12, decimal_places=2,)
    channel = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    impressions = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.channel}({self.os})'

    @property
    def cpi(self):
        return self.spend / self.installs