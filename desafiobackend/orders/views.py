# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from .models import Order
from .util import id_generator
import time

# Create your views here.
def orders(request):
	context = {}
	template = "orders/user.html"
	return render(request, template, context)

@login_required
def checkout(request):
	
	try:
		the_id = request.session['cart_id'] #Checa se exite sessão
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
		return HttpResponseRedirect(reverse("cart"))

	try:
		# Tenta buscar um pedido associado ao carrinho
		new_order = Order.objects.get(cart=cart)
	except Order.DoesNotExist:
		# Caso não exista cria uma instância associado a esse acrrinho
		new_order = Order()
		new_order.cart = cart
		new_order.user = request.user
		new_order.order_id = id_generator()
		new_order.save()

	# Se o status é finalizado remove o id do carrinho e seus itens, 
	# mas não o exclui do banco de dados
	if new_order.status == "Finished":
		del request.session['cart_id']
		del request.session['items_total']
		return HttpResponseRedirect(reverse("cart"))

	context = {}
	template = 'products/home.html'

	return render(request, template, context)