# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Countries(models.Model):
    country_id = models.CharField(primary_key=True, max_length=2)
    country_name = models.CharField(max_length=40, blank=True)
    region_id = models.ForeignKey('Regions', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'countries'

class Departments(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=30)
    manager = models.ForeignKey('Employees', blank=True, null=True)
    location = models.ForeignKey('Locations', blank=True, null=True)
    def __unicode__(self):
        return self.department_name
    class Meta:
        managed = False
        db_table = 'departments'

class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=25)
    email = models.CharField(unique=True, max_length=25)
    phone_number = models.CharField(max_length=20, blank=True)
    hire_date = models.DateField()
    job = models.ForeignKey('Jobs')
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    commission_pct = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    manager = models.ForeignKey('self', blank=True, null=True)
    department = models.ForeignKey(Departments, blank=True, null=True)
    def __unicode__(self):
      return self.first_name +' '+self.last_name
    class Meta:
        managed = False
        db_table = 'employees'


class JobHistory(models.Model):
    employee = models.ForeignKey(Employees)
    start_date = models.DateField()
    end_date = models.DateField()
    job = models.ForeignKey('Jobs')
    department = models.ForeignKey(Departments, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'job_history'

class Jobs(models.Model):
    job_id = models.CharField(primary_key=True, max_length=10)
    job_title = models.CharField(max_length=35)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'jobs'

class Locations(models.Model):
    location_id = models.IntegerField(primary_key=True)
    street_address = models.CharField(max_length=40, blank=True)
    postal_code = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=25, blank=True)
    country_id = models.CharField(max_length=2, blank=True)
    class Meta:
        managed = False
        db_table = 'locations'

class Regions(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_name = models.CharField(max_length=25, blank=True)
    class Meta:
        managed = False
        db_table = 'regions'

