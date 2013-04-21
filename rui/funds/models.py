from __future__ import unicode_literals
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

# class AuthGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=80)
#     class Meta:
#         managed = False
#         db_table = 'auth_group'

# class AuthGroupPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group_id = models.IntegerField()
#     permission_id = models.IntegerField()
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'

# class AuthPermission(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     content_type_id = models.IntegerField()
#     codename = models.CharField(max_length=100)
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'

# class AuthUser(models.Model):
#     id = models.IntegerField(primary_key=True)
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField()
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=75)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#     class Meta:
#         managed = False
#         db_table = 'auth_user'

# class AuthUserGroups(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.IntegerField()
#     group_id = models.IntegerField()
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'

# class AuthUserUserPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.IntegerField()
#     permission_id = models.IntegerField()
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'

# class DjangoAdminLog(models.Model):
#     id = models.IntegerField(primary_key=True)
#     action_time = models.DateTimeField()
#     user_id = models.IntegerField()
#     content_type_id = models.IntegerField(blank=True, null=True)
#     object_id = models.TextField(blank=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.IntegerField()
#     change_message = models.TextField()
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'

# class DjangoContentType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100)
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'

# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#     class Meta:
#         managed = False
#         db_table = 'django_session'


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
        return unicode(self.id)
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
        return unicode(self.id)
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
        return unicode(self.id)
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
        return unicode(self.id)
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
        return unicode(self.id)
    class Meta:
        db_table = 'Luokittelemattomat'
