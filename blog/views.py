from django.shortcuts import render
from rest_framework.decorators import api_view
from . models import *
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from . serializer import *
# Create your views here.
class Blog:
	login=""
	@api_view(["get"])
	def getlogin(request):
		print(Blog.login)
		output = [{"login" : Blog.login}]
		print(output)
		return Response(output)
	@api_view(["PUT"])
	def setlogin(request):
		Blog.login=request.data['log']
		print("in put login : ",Blog.login)
		return Response("updated login done!")
	@api_view(['get'])
	def Usernameget(request):
			output=[{'username':output.username,'password':output.password,'email':output.email}for output in Users.objects.all()]
			print(output)
			return Response(output)
	@api_view(['post'])
	def Usernamepost(requset):
			print(requset.data)
			serializers=User(data = requset.data)
			if serializers.is_valid(raise_exception=True):
				serializers.save()
				return Response("done with Posting data !")
	@api_view(['delete'])
	def Usernamedelete(request, usernames):
		print(request.data)
		sn=Users.objects.get(username=usernames)
		print(sn)
		sn.delete()
		return Response("success!!")

	@api_view(['get'])
	def BlogGet(request):
		output = [ {'text_data':output.text_data,'title':output.title } for output in BlogInfo.objects.all()]
		return Response(output)
	@api_view(["POST"])
	def BlogPost(request):
		serializers=BlogSerializer(data=request.data)
		if serializers.is_valid(raise_exception=True):
			print(serializers)
			serializers.save()
			return Response(serializers.data)
	@api_view(["delete"])
	def Blogdelete(request, id):
		blog=BlogInfo.objects.get(text_id=id)
		blog.delete()
		return Response("deleted the blog contents .. success!!")
	@api_view(["PUT"])
	def Blogput(request, id, td):
		blog=BlogInfo.objects.get(text_id=id)
		blog.text_data=td
		return Response("updated succesfully !!")
	@api_view(["get"])
	def BlogId(request):
		blog=BlogInfo.objects.all()