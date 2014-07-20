#models.py for the Novella LMS API
#Programmers: Affan, Sen
#
#
#




from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#This will be the main profile model. It has a one-to-one relationship with the built-in django user class
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	email = models.EmailField(blank=True)
	#photo = models.ImageField(blank=True)
	website = models.URLField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	closed = models.DateTimeField(blank=True)
	status = models.CharField(max_length=30,blank=True)

	def __unicode__(self):
		return (self.first_name + " " + self.last_name + " | " + self.user.username)


