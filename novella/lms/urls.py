from django.conf.urls import patterns, url
from django.conf.urls.defaults import *
from myapp.api import EntryResource

from lms import views

student_resource = StudentResource()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.auth_and_login, name='login'),
    url(r'^register/$', views.sign_up_in, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^loginform/$', views.loginform, name='weblogin'),
    url(r'^students/', include('student_resource.urls')),

)