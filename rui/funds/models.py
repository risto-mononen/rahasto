from __future__ import unicode_literals
from django.db import models

from django.db import models


class Hedgerahastot(models.Model):
    rahasto = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    valuutta = models.CharField(max_length=255, blank=True)
    arvo = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pv1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pvm = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return self.rahasto
    class Meta:
        db_table = 'Hedgerahastot'

class Korkorahastot(models.Model):
    rahasto = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    valuutta = models.CharField(max_length=255, blank=True)
    arvo = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pv1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pvm = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return self.rahasto
    class Meta:
        db_table = 'Korkorahastot'

class Osakerahastot(models.Model):
    rahasto = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    valuutta = models.CharField(max_length=255, blank=True)
    arvo = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pv1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pvm = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return self.rahasto
    class Meta:
        db_table = 'Osakerahastot'

class Yhdistelmarahastot(models.Model):
    rahasto = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    valuutta = models.CharField(max_length=255, blank=True)
    arvo = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pv1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pvm = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return self.rahasto
    class Meta:
        db_table = 'Yhdistelmarahastot'

class Luokittelemattomat(models.Model):
    rahasto = models.CharField(max_length=255, blank=True)
    rating = models.CharField(max_length=255, blank=True)
    valuutta = models.CharField(max_length=255, blank=True)
    arvo = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pv1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    kk6 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v1 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    v3 = models.DecimalField(max_digits=21, decimal_places=4, blank=True, null=True)
    pvm = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return self.rahasto
    class Meta:
        db_table = 'Luokittelemattomat'
