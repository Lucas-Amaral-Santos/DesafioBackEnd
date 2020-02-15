# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.core.urlresolvers import reverse
from .forms import LoginForm, RegistrationForm
# Create your views here.

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def login_view(request):

	# Requisita Login.py através do método POST
	# caso não esteja preenchido não faz nada
	form = LoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)
		return HttpResponseRedirect(reverse("home"))


	context = {
		"form": form
	}
	return render(request, "forms.html", context)

def registration_view(request):
	form = RegistrationForm(request.POST or None)

	if form.is_valid():
		new_user = form.save(commit=False)
		new_user.save()


	context = {
		"form": form
	}
	return render(request, "forms.html", context)		