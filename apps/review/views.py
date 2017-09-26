# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .models import User
from .models import Review, Author, Book

def home(request):
	if 'user_id' in request.session:
		user = User.objects.get(id = request.session['user_id'])
		reviews = Review.objects.all()
		context = {
			'user': user,
			'reviews': reviews,
		}
		print reviews
		return render(request, 'review/home.html', context)
	return redirect(reverse('landing'))

def add(request):
	if 'user_id' in request.session:
		user = User.objects.get(id = request.session['user_id'])
		
		context = {
			'user': user,
			"authors": Author.objects.all()
		}
	
		return render(request, 'review/add.html', context)
	return redirect(reverse('landing'))

def create(request):
	errors = Review.objects.validate_review(request.POST)
    	if errors:
			for error in errors:
				messages.error(request, error)
  			else:
				review = Review.objects.create_review(request.POST, request.session['user_id'])
			return redirect(reverse('home'))

def show(request):
	pass