from django.shortcuts import render, Http404

from .models import Product
# Create your views here.

def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		products = Product.objects.filter(title__icontains=q)
		context = {'query': q, 'products':products}
		template = 'products/results.html'
	else:
		template = 'products/home.html'
		context = {}
	return render(request, template, context)

def home(request):
	products = Product.objects.all()
	if request.user.is_authenticated():
		
		context = {'username_is': request.user,
					'products':products}
	else:
		context = {'username_is': request.user,
					'products':products}

	template = 'products/home.html'
	return render(request, template, context)

def all(request):
	products = Product.objects.all()
	context = {'products': products}
	template = 'products/all.html'

	return render(request, template, context)

def single(request, slug):

	product = Product.objects.get(slug=slug)
	images = product.productimage_set.all()
	context = {'product': product, 'images':images}
	template = 'products/single.html'
	return render(request, template, context)