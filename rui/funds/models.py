from __future__ import unicode_literals
from django.db import models

from django.db import models


class Hedge(models.Model):
    fund = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    currency = models.CharField(max_length=255, blank=True)
    nav = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    day1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return fund_unicode(self)
    class Meta:
        db_table = 'Hedge'

class Bond(models.Model):
    fund = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    currency = models.CharField(max_length=255, blank=True)
    nav = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    day1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return fund_unicode(self)
    class Meta:
        db_table = 'Bond'

class Stock(models.Model):
    fund = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    currency = models.CharField(max_length=255, blank=True)
    nav = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    day1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return fund_unicode(self)
    class Meta:
        db_table = 'Stock'

class Balanced(models.Model):
    fund = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    currency = models.CharField(max_length=255, blank=True)
    nav = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    day1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return fund_unicode(self)
    class Meta:
        db_table = 'Balanced'

class Unclassified(models.Model):
    fund = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    currency = models.CharField(max_length=255, blank=True)
    nav = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    day1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    month6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    year3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return fund_unicode(self)
    class Meta:
        db_table = 'Unclassified'

def fund_unicode(obj):
    return reduce(lambda x, y: str(x)+'\t|\t'+str(y),
                  (obj.fund, obj.rating, obj.currency,
                   obj.nav, obj.day1, obj.month3, obj.month6,
                   obj.year1, obj.year3, obj.date))
