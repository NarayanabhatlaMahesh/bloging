from django.db import models

# Create your models here.
 
class Users(models.Model):
	username=models.TextField(unique= True)
	password=models.TextField()
	email=models.TextField()

class BlogInfo(models.Model):
	title=models.CharField(max_length=100)
	text_data=models.TextField(unique=True)