# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=45)
	address = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name

class Sneaker(models.Model):
	brand = models.CharField(max_length=45)
	color = models.CharField(max_length=45)
	
	def __str__(self):
		return self.brand

class Clothes(models.Model):
	brand = models.CharField(max_length=45)
	size = models.CharField(max_length=45)
	
	def __str__(self):
		return self.brand
