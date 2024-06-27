from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from . models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token



from . serializer import *
# Create your views here.
def getAuth(key,userobj):
	authorized = False
	authtoken = Token.objects.get_or_create(user=userobj)
	if(authtoken):
		if(authtoken is key):
			authorized=True
	return authorized
login=""
@api_view(["get"])
def getlogin(request):
	print('in get login ',request)
	# Response.delete_cookie(Token)

	print(Token.key)
	output = [{"login" : login}]
	return Response(output)

@api_view(["PUT"])
def setlogin(request):
	login=request.PUT
	print('session name should print now')
	print(login)
	return Response("updated login done!")

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(['post'])
def Usernamepost(request):
		serializers=Users.objects.create_user(username=request.data['username'],email='jambalakadipamba@gmail.com',password=request.data['password'], date_of_birth='2000-11-21')
		return Response('User Created Succesfully')

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(['delete'])
def Usernamedelete(request, usernames):
	sn=Users.objects.get(username=usernames)
	sn.delete()
	return Response("success!!")

def generatesomeresp(request):
	return JSONRenderer({'hell':'is closer'})