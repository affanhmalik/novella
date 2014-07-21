from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('quiz/index.html')
    return HttpResponse("Hello, world. You're at the poll index.")