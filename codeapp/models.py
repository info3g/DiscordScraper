from django.db import models

# Create your models here.


class recent(models.Model):
	title = models.CharField(max_length=1000000,blank=True, null=True)

class search(models.Model):
	search = models.CharField(max_length=10000,blank=True, null=True)

class listofuser(models.Model):
	list_of_user = models.CharField(max_length=10000,blank=True, null=True)