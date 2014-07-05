from django.conf.urls import patterns, url

from lms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.auth_and_login, name='login'),
    url(r'^register/$', views.sign_up_in, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^loginform/$', views.loginform, name='weblogin'),

)