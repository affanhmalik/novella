from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
	# student = models.ForeignKey(User)
	# course = models.ForeignKey('Course',related_name = 'quiz') 
	quizName = models.CharField(max_length=200)
	introduction = models.TextField(max_length=800)
	timeLimit = models.IntegerField(default=5)
	grade = models.FloatField(default=0)

	def __unicode__(self):
		return self.quizName


class Question(models.Model):
	quiz = models.ForeignKey('Quiz', related_name = 'questions')
	text = models.TextField(max_length=800)
	choiceA = models.CharField(max_length=200)
	choiceB = models.CharField(max_length=200)
	choiceC = models.CharField(max_length=200)
	choiceD = models.CharField(max_length=200)
	corrAns = models.CharField(max_length=50)
	response = models.CharField(max_length=50, default=None, blank=True)

	def __unicode__(self):
		return self.text

