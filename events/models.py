from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.

class Event_manager(models.Manager):
	def create_event(self, post_data):
		print('--- ATTEMPTING validate event ---')
		response_to_views = {}
		errors = []
		if len(post_data['name']) < 1:
			errors.append("Your event must have a name.")
		if len(post_data['desc']) < 10:
			errors.append("Try giving your event a longer description.")
		if deadline == 0:
			errors.append("You must add an RSVP deadline.")

		else:
			response_to_views['errors'] = 0
			response_to_views['status'] = True
			print('--- VALIDATIONS passed ---')
			event = self.create(name = post_data['name'], desc = post_data['desc'], tags = post_data['tags'], location = post_data['location'])

class Event(models.Model):
	name = models.CharField(max_length=20, default = False)
	desc = models.CharField(max_length=140, default = False)
	tags = models.CharField(max_length=140, default = False)
	location = models.CharField(max_length=140, default = False)
	rsvp_date = models.DateField(default=date.today)
	created_at = models.DateTimeField(default=timezone.now)
	objects = Event_manager()