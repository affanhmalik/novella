from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.resources import ALL
from tastypie.serializers import Serializer
from course.models import Course, Section, Lecture, Content, Assignment, Notification

class SectionResource(ModelResource):


	class Meta:
		queryset = Section.objects.all()
