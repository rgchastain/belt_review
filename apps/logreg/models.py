# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):
	def validate_registration(self, form_data):
		errors = []

		if len(form_data['name']) == 0:
			errors.append('Name is required.')
		if len(form_data['alias']) == 0:
			errors.append('Alias is required.')
		if len(form_data['email']) == 0:
			errors.append('Email is required.')
		# if email = form_data['email']:
		# 	errors.append("email already in use")
		if len(form_data['password']) == 0:
			errors.append('Password is required.')
		if form_data['password'] != form_data['password_confirmation']:
			errors.append('Passwords must match.')

		return errors

	def validate_login(self, form_data):
		errors = []
        # check DB for post_data['email']
		if len(self.filter(email=form_data['email'])) > 0:
            # check this user's password
			user = self.filter(email=form_data['email'])[0]
			if not bcrypt.checkpw(form_data['password'].encode(), user.password.encode()):
				errors.append('email/password incorrect')
		else:
			errors.append('email/password incorrect')

		if errors:
			return errors

		return user
	
	def create_user(self, form_data):
		hashedpw = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt())

		return User.objects.create(
			name = form_data['name'],
			alias = form_data['alias'],
			email = form_data['email'],
			password = hashedpw,
		)


class User(models.Model):
	name = models.CharField(max_length = 50)
	alias = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()

