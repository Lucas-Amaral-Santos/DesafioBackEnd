# -*- coding: utf-8 -*
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
	email = forms.EmailField(label='Informe o email.')
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data.get("username")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError('Usuário inexistente.')
		return username

	def clean_password(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		try:
			user = User.objects.get(username=username)
		except:
			user = None
		if user is not None and not user.check_password(password):
			raise forms.ValidationError('Senha incorreta.')			
		elif user is None:
			pass
		else:
			return password

class RegistrationForm(forms.ModelForm):
	password1 = forms.CharField(label="Informe a senha", widget=forms.PasswordInput())
	password2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput())


	class Meta:
		model = User
		fields = ['username', 'email']

		def clean_password(self):
			password1 = self.cleaned_data.get('password1')
			password2 = self.cleaned_data.get('password2')

			if password1 and password2 and password1 != password2:
				raise forms.ValidationError('Senhas incompatíveis.')
			return password2	

		def clean_email(self):
			email = self.cleaned_data.get("email")
			user = User.objects.filter(email=email).count()
			if user_count > 0:
				 raise forms.ValidationError('Email já está em uso.')
			return email

		def save(self, commit=True):
			user = super(RegistrationForm, self).save(commit=False)
			user.set_password(self.cleaned_data['password1'])
			if commit:
				user.save()
			return user
