"""desafiobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from products import views
import carts.views as cart
import orders.views as order
import users.views as user
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^s/$', views.search, name='search'),
	url(r'^products/$', views.all, name='products'),
	url(r'^products/(?P<slug>[\w-]+)/$', views.single, name='single_product'),
	url(r'^cart/(?P<id>\d+)/$', cart.remove_from_cart, name='remove_from_cart'),    
	url(r'^cart/(?P<slug>[\w-]+)/$', cart.add_to_cart, name='add_to_cart'),    
  url(r'^cart/$', cart.view, name='cart'),
  url(r'^checkout/$', order.checkout, name='checkout'),
  url(r'^orders/$', order.orders, name='user_orders'),

  url(r'^users/logout/', user.logout_view, name='auth_logout'),
  url(r'^users/login/', user.login_view, name='auth_login'),
  url(r'^users/register/', user.registration_view, name='auth_register'),

  url(r'^admin/', admin.site.urls),
] 

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)