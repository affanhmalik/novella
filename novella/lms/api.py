# myapp/api.py for the Novella LMS API
#Programmers: Ben
#
#
#


from tastypie.resources import ModelResource
from lms.models import Student

class StudentResource(ModelResource):
	class Meta:
		queryset = Student.objects.all()
		resource_name = 'student'