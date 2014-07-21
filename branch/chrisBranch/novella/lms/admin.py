from django.contrib import admin
from course.models import Course, Section, Lecture, Content, Assignment, Notification
from lms.models import Student, Instructor, Enrollment

class SectionInline(admin.TabularInline):
	model = Section

class CourseAdmin(admin.ModelAdmin):
	inlines = [
		SectionInline,
	]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture)
admin.site.register(Content)
admin.site.register(Assignment)
admin.site.register(Notification)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(Section)
#admin.site.register()

