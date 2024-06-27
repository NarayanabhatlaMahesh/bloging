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
from blog.views import getAuth
from .serializer import BlogSerializer


@api_view(['get'])
@authentication_classes([])
@permission_classes([])
def BlogGet(request):
	output = [ {'text_data':output.text_data,'title':output.title } for output in BlogInfo.objects.all()]
	return Response(output)


@authentication_classes([SessionAuthentication, BasicAuthentication])
@api_view(["POST"])
def BlogPost(request):
	serializers=BlogSerializer(data=request.data)
	if serializers.is_valid(raise_exception=True):
		print('serializers')
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
