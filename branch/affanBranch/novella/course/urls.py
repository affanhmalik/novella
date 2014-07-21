from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api import SectionResource

course_resource = CourseResource()

# v1_api = Api(api_name='v1')
# v1_api.register(QuizResource())
# v1_api.register(QuestionResource())

urlpatterns = patterns('',
	# url(r'^api/',include(v1_api.urls)),
	url(r'api/', include(course_resource.urls)),
	
)