from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField
#https://github.com/bradjasper/django-jsonfield

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=240)

	def __unicode__(self):
		return self.name

class Recipe(models.Model):
	package_name = models.CharField(max_length=250)
	json = JSONField()
	category = models.ForeignKey(Category, blank=True, null = True)

	def __unicode__(self):
		return self.package_name

class Update(models.Model):
	last_update = models.CharField(max_length=240)

	def __unicode__(self):
		return self.last_update
