from rest_framework import serializers
from . models import *

class User(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ["username","password","email"]
class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlogInfo
		fields = ["title","text_data"]