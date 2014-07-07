from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#This will be the main student model. It has a one-to-one relationship with the built-in django user class
class Student(models.Model):
	studentid = models.ForeignKey(User)
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	email = models.CharField(max_length=60)

class Instructor(models.Model):
	instid = models.ForeignKey(User)
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)


