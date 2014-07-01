from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from django.http import HttpResponse

# Create your views here.

# If we want to use a web-login, we can use this view
def loginview(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)


# The main authentication function for a registered user, the success and fail redirects can be changed
def auth_and_login(request, onsuccess='/', onfail='/login/'):
	user = authenticate(username=request.POST['email'], password=request.POST['password'])
	if user is not None:
		login(request, user)
		return redirect(onsuccess)
	else:
		return redirect(onfail)


# View funciton for signing up a new user
def sign_up_in(request):
	post = request.POST
	if not user_exists(post['email']):
		user = create_user(username=post['email'], email=post['email'], password=post['password'])
		return auth_and_login(request)
	else:
		return redirect("/login/")

# Create a new user with the request credentials
def create_user(username,email,password):
	user = User(username=username, email=email)
	user.set_password(password)
	user.save()
	return user

# Check to see if username exists or not
def user_exists(username):
	user_count = User.objects.filter(username=username).count()
	if user_count == 0:
		return False
	return True

# Dummy base view for /lms
def index(request):
	data = {}
	data['version'] = '1.0'
	data['title'] = 'Novella Learning Management System API'
	data['status'] = 200
	data['message'] = 'Hello Team Too developer! Welcome to Novella. You have reached the main page of the API. The documentation is building up at lightning speed. So looks like you wont have to wait too long. See you back in a bit! - We got your back, Group J'
	return HttpResponse(json.dumps(data), content_type = "application/json")

