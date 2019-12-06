from django.db import models
from multiselectfield import MultiSelectField

class acquisition(models.Model):
	# image = models.ImageField(upload_to='acquisition', blank=True)
	# image = (
	# 	('test1', 'test1'),('test2', 'test2'),('test3', 'test3'),('test3', 'test4'),
	# 	)
	# title = MultiSelectField(choices = image)
	title = models.CharField(max_length=100, default=True)
	author = models.CharField(max_length=100, default=True)
	pdf = models.FileField(upload_to='books/pdfs/', blank=True, null=True)
	# image = models.ImageField(upload_to='acquisition_images/', blank=True, null=True)

	def __str__(self):
		return self.title
