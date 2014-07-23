from django.contrib import admin
from course.models import Course, Section, Lecture, Content, Assignment, Notification
from lms.models import Student, Instructor, Enrollment

class SectionInline(admin.StackedInline):
	model = Section


class CourseAdmin(admin.ModelAdmin):
	inlines = [
		SectionInline,
	]

class ContentInline(admin.StackedInline):
	model = Content
	
class LectureAdmin(admin.ModelAdmin):
	inlines = [
		ContentInline,
	]



admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Content)
admin.site.register(Assignment)
admin.site.register(Notification)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Enrollment)
admin.site.register(Section)
#admin.site.register()

