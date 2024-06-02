from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import BaseUser

# Create your models here.
 
class Users(AbstractBaseUser):
	email = models.EmailField(("email address"), unique=True)
	name=models.TextField(max_length=1000, unique=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	date_of_birth = models.DateField()
	REQUIRED_FIELDS = ["date_of_birth"]
	USERNAME_FIELD = "name"

	objects = BaseUser()

	def __str__(self):
		return self.email

class BlogInfo(models.Model):
	title=models.CharField(max_length=100)
	text_data=models.TextField(unique=True)