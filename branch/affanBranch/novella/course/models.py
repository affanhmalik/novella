from django.db import models

# Create your models here.

class Course(models.Model):
	courseCode = models.CharField(max_length=25,default="No code yet")
	title = models.TextField(blank=True)
	start = models.DateField(blank=True)
	end = models.DateField(blank=True)


	def __unicode__(self):
		return self.courseCode

class Lecture(models.Model):
	course = models.ForeignKey(Course)
	lectureCode = models.CharField(max_length=25,default="No code yet")
	weekNumber = models.IntegerField(default="No week number assigned")

	def __unicode__(self):
		return (self.course.courseCode + ">" + self.lectureCode)

class Content(models.Model):
	course = models.ForeignKey(Lecture)
	contentCode = models.CharField(max_length=25,default="No code yet")
	title = models.TextField(blank=True)
	body = models.TextField(blank=True)

	def __unicode__(self):
		return (self.course.courseCode + ">" + self.lectureCode + ">" + self.contentCode)

class Assignment(models.Model):
	course = models.ForeignKey(Course)
	assignmentCode = models.CharField(max_length=25,default="No code yet")
	postedDate = models.DateTimeField(auto_now_add=True)
	dueDate = models.DateTimeField(blank=True)
	title = models.TextField(blank=True)
	body = models.TextField(blank=True)
	#mainFile = models.FileField(blank=True)
	#markingFile = models.FileField(blank=True)
	maxGrade = models.IntegerField(default=0)
	weight = models.IntegerField(default=0)
	status = models.CharField(max_length=25,default="active")

	def __unicode__(self):
		return (self.course.courseCode + ">" + self.assignmentCode)


