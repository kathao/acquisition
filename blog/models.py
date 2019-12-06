from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100, default='')
	content = models.TextField(default='')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
	address = models.CharField(max_length=100, default='')
	city_state = models.CharField(max_length=100, default='')
	price = models.CharField(max_length=100, default='')
	beds = models.CharField(max_length=100, default='')
	sq_ft = models.CharField(max_length=100, default='')
	website = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})	

class Book(models.Model):		
	title = models.CharField(max_length=100, default='')
	name = models.CharField(max_length=100, default='')
	image = models.ImageField(upload_to='acquisition_images', null=True, blank='')

	def __str__(self):
		return self.title

class Rsvp(models.Model):		
	name = models.CharField(max_length=100, default='')
	address = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	state = models.CharField(max_length=100, default='')
	zip_code = models.CharField(max_length=100, default='')
	email = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.name

class Rsvp_template(models.Model):
	title = models.CharField(max_length=100, default='')
	image = models.ImageField(upload_to='event_images', null=True, blank='')

	def __str__(self):
		return self.title