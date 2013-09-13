# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from golem.models import Alarm

def index_view(request):
	return render_to_response("index.html")

def login_view(request):
	context = RequestContext(request)
	if request.method == "GET":
		return render_to_response("login.html",context_instance=context)
	else:
		try:
			username = request.POST['login-username']
			password = request.POST['login-password']
		except KeyError:
			return HttpResponseBadRequest("Need to include all required parameters: login-username, login-password")
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return HttpResponseRedirect("/main")
			else:
				return HttpResponseForbidden("Your user is inactive")
		else:
			return HttpResponseForbidden("Incorrect username or password")

@login_required
def main_view(request):
	c = RequestContext(request, {"alarms":Alarm.objects.all()})
	return render_to_response("main.html", context_instance=c)
	
@login_required
def logout_view(request):
	auth.logout(request)
	return HttpResponseRedirect("/")
	
@login_required
def test_display_view(request):
	import pika as p
	
	connection = p.BlockingConnection(p.ConnectionParameters("localhost"))
	channel = connection.channel()
	
	channel.basic_publish(exchange = "",
												routing_key = "commands",
												body = "displaytest")
												
	connection.close()
	
	return HttpResponse()
