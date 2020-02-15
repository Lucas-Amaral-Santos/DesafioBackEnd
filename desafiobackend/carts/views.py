# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from products.models import Product, Variation
# Create your views here.
from models import Cart, CartItem


#------------ Pedido feito a um Carrinho de compras----------------------- 
def view(request):
	try:
		the_id = request.session['cart_id'] #Checa se exite sessão
		cart = Cart.objects.get(id=the_id)
	except:
		the_id = None
	if the_id:
		#--------ATUALIZANDO O PREÇO TOTAL DO CART----------
		aux = 0.00
		for item in cart.cartitem_set.all():
			line_total = float(item.product.price) * item.quantity
			aux += line_total

		request.session['items_total'] = cart.cartitem_set.count()
		cart.total = aux
		cart.save()

		context = {"cart": cart}
	else:
		empty_message = "Seu carrinho está vazio! :("
		context = {"empty":True, "empty_message": empty_message}
	template = "cart/view.html"
	return render(request, template, context)


def remove_from_cart(request, id):

	# Checando se o carrinho existe
	try:
		the_id = request.session['cart_id'] #Checa se exite sessão
		cart = Cart.objects.get(id=the_id)
	except:
		return HttpResponseRedirect(reverse("cart"))

	# Buscando o carrinho e removendo 
	cartitem = CartItem.objects.get(id=id)
	#cartitem.delete()
	cartitem.cart = None
	cartitem.save()

	return HttpResponseRedirect(reverse("cart"))

def add_to_cart(request, slug):
	request.session.set_expiry(120000)

	try:
		the_id = request.session['cart_id'] #Checa se exite sessão
	except: # Cria nova sessão
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id)

	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		pass
	except:
		pass

	#---------------------USANDO POST-------------------
	product_var = []
	if request.method == "POST":
		qty = request.POST['qty']

		for item in request.POST:
			key = item
			val = request.POST[key]
			try:
				v = Variation.objects.get(product=product, category_ixact=key, title_iexact=val)
				product_var.append(v)
			except:
				pass
	#---------------------USANDO GET --------------------
	# try:
	# 	qty = request.GET.get('qty')
	# 	size = True
	# except:
	# 	qty = None
	# 	update_qty = False

	# notes = {}
	# try:
	# 	color = request.GET.get('color')
	# 	notes['color'] = color
	# 	print color
	# except:
	# 	color = None

	# try:
	# 	size = request.GET.get('size')
	# 	notes['size'] = size
	# 	print size
	# except:
	# 	size = None



	#-----------CRIANDO UMA SESSÃO ------------------------

		cart_item = CartItem.objects.create(cart=cart, product=product)

		if len(product_var)>0:
			cart_item.variations.add(*product_var)
		cart_item.quantity = qty
		cart_item.save()

	# if not cart_item in cart.items.all():
	# 	cart.items.add(cart_item)
	# else:
	# 	cart.items.remove(cart_item)

	
		return HttpResponseRedirect(reverse("cart"))
	else:
		return HttpResponseRedirect(reverse("cart"))

