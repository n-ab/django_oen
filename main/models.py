from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
# from login.models import User

class User_manager(models.Manager):
	def create_user(self, post_data):
		print('--- ATTEMPTING validate user ---')
		response_to_views = {}
		errors = []
		if len(post_data['first_name']) < 1:
			errors.append("First Name cannot be blank.")
		if len(post_data['last_name']) < 1:
			errors.append("Last Name cannot be blank.")
		if len(post_data['username']) < 1:
			errors.append("Username cannot be blank.")
		if len(post_data['email']) < 1:
			errors.append("Email cannot be blank.")
		if errors:
			response_to_views['status'] = False
			response_to_views['errors'] = errors
		else:
			response_to_views['errors'] = 0
			response_to_views['status'] = True
			print('--- VALIDATIONS passed ---')
			hashedpassword = bcrypt.hashpw(post_data['pword'].encode(), bcrypt.gensalt())
			user = self.create(first_name = post_data['first_name'], last_name = post_data['last_name'], username = post_data['username'], email = post_data['email'], zipcode = post_data['zipcode'], pword = hashedpassword, status = True)
			response_to_views['user'] = self.name
			response_to_views['errors'] = []
			print(hashedpassword)
			print('--- ADDED '+response_to_views['user']+' ---')
			return response_to_views
	def login_user(self, post_data):
		print('--- ATTEMPTING validate login ---')
		response_to_views = {}
		user = User.objects.get(email = post_data['field1'])
		print(user)
		if user:
			if(bcrypt.checkpw(post_data['field2'].encode(), user.pword.encode())):
				response_to_views['status'] = True
				response_to_views['user'] = user
			else:
				response_to_views['status'] = False
				response_to_views['errors'] = 'Invalid Entry'
		else:
			response_to_views['status'] = False
			response_to_views['errors'] = 'Invalid Entry'
		return response_to_views

class User(models.Model):
	first_name = models.CharField(max_length=20, default = False)
	last_name = models.CharField(max_length=20, default = False)
	username = models.CharField(max_length=20, default = False)
	email = models.CharField(max_length=20, default = False)
	zipcode = models.CharField(max_length=5, default = False)
	pword = models.CharField(max_length=20, default = False)
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(default=timezone.now)
	objects = User_manager()
class Organization(models.Model):
	title = models.CharField(blank=False, max_length=20)
	address = models.CharField(blank=False, max_length=20)
	users = models.ManyToManyField(User, related_name="organizations")


