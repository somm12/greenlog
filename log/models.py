from django.db import models

class Post(models.Model):
    kinds = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField()
    



class Plogging(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField()
    firstPlace = models.CharField(max_length=30)
    like=models.IntegerField()



class User(models.Model):
    name = models.CharField(max_length=10)
    id = models.CharField(max_length=10,primary_key=True)
    password =models.CharField(max_length=20)
    nickname =models.CharField(max_length=10)
    profile = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
