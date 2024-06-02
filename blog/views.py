from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from . models import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from django.contrib.auth import get_user_model
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.sessions.models import Session


from . serializer import *
# Create your views here.
login=""
@api_view(["get"])
def getlogin(request):
	print('in get login ',request.user)
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
@api_view(['get'])
def Usernameget(request):
	login=request.GET
	print('get',login)
	userobj = Users.objects.get(name='username0')
	token = Token.objects.get(user=userobj)
	print('usernameget token is ',token.key)
	return Response("eys")

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(['post'])
def Usernamepost(request):
		users = Users()
		serializers=Users.objects.create_user(username=request.data['username'],email='jambalakadipamba@gmail.com',password=request.data['password'], date_of_birth='2000-11-21')
		return Response('created i guess')

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(['delete'])
def Usernamedelete(request, usernames):
	sn=Users.objects.get(username=usernames)
	sn.delete()
	return Response("success!!")

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(['get'])
def BlogGet(request):
	output = [ {'text_data':output.text_data,'title':output.title } for output in BlogInfo.objects.all()]
	return Response(output)


@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(["POST"])
def BlogPost(request):
	serializers=BlogSerializer(data=request.data)
	if serializers.is_valid(raise_exception=True):
		print(serializers)
		serializers.save()
		return Response(serializers.data)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(["delete"])
def Blogdelete(request, id):
	blog=BlogInfo.objects.get(text_id=id)
	blog.delete()
	return Response("deleted the blog contents .. success!!")

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(["PUT"])
def Blogput(request, id, td):
	blog=BlogInfo.objects.get(text_id=id)
	blog.text_data=td
	return Response("updated succesfully !!")

@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(["get"])
def BlogId(request):
	blog=BlogInfo.objects.all()

def generatesomeresp(request):
	return JSONRenderer({'hell':'is closer'})