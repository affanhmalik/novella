from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.resources import ALL
from tastypie.serializers import Serializer
from quiz.models import Quiz, Question

class QuestionResource(ModelResource):
	# quiz = fields.ForeignKey(QuizResource, 'quiz')

	class Meta:
		queryset = Question.objects.all()
		# resource_name = 'quiz/question'
		include_resource_uri = False
		excludes = ['id']
		# serializer = Serializer()

class QuizResource(ModelResource):
	questions = fields.ToManyField('quiz.api.QuestionResource','questions',full=True)

	class Meta:
		queryset = Quiz.objects.all()
		resource_name = 'quiz'
		# excludes = ['id']
		include_resource_uri = False
		# serializer = Serializer()
