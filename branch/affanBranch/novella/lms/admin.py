from django.contrib import admin
from course.models import Course, Lecture, Content, Assignment

# Register your models here.

admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Content)
