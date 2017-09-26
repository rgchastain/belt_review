# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..logreg.models import User
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books")



class ReviewManager(models.Manager):
	def validate_review(self, form_data):
		errors = []
		if len(form_data['title']) < 1 or len(form_data['review']) <1:
			errors.append('required fields')
		if not "author" in form_data and len(form_data['new_author']) < 3:
			errors.append('new author names must 3 or more characters')
		return errors
		if "author" in form_data and len(form_data['new_author']) > 0 and len(form_data['new_author']) < 3:
			errors.append('new author names must 3 or more characters')
       		return errors
	def create_review(self, new_data, user_id):
		authors = Author.objects.create(name = new_data['new_author'])
		books = Book.objects.create(title = new_data['title'], author = authors)
		return Review.objects.create(
			review = new_data['review'],
			rating = new_data['rating'],
			book = books,
			reviewer = User.objects.get(id=user_id)
			
		)



class Review(models.Model):
	review = models.TextField()
	rating = models.IntegerField()
	book = models.ForeignKey(Book, related_name="reviews")
	reviewer = models.ForeignKey(User, related_name="reviews_left")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = ReviewManager()


