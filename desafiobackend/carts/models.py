# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from products.models import Product, Variation

class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True)
	product = models.ForeignKey(Product)
	variations = models.ManyToManyField(Variation, null=True, blank=True)
	quantity = models.IntegerField(default=1)	
	line_total = models.DecimalField(default=10.99, max_digits=100, decimal_places=2)
	notes = models.TextField(null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
		try:
			return str(self.product.id)
		except:
			return self.product.title
		

# Create your models here.

#--------Entidade PEDIDO--------------------------------

class Cart(models.Model):
	"""docstring for Cart"models.Model
	"""
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)


	def __unicode__(self):
		return "Cart id: %s" %(self.id)