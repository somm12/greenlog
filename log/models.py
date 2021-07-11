from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10,default='')
    nickname = models.CharField(max_length=10,primary_key=True)
    password =models.CharField(max_length=20,default='')
    profile = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    Member =models.CharField(max_length=10,default='')

class Post(models.Model):
    kinds = models.CharField(max_length=10,default='')
    title = models.CharField(max_length=30,default='')
    writer =  models.ForeignKey(User ,on_delete=models.CASCADE,default='') 
    content = models.TextField(default='')
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField(default='')

class Plogging(models.Model):
    title = models.CharField(max_length=30,default='')
    writer =  models.ForeignKey(User ,on_delete=models.CASCADE,default='') 
    content = models.TextField(default='')
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField(default='')
    firstPlace = models.CharField(max_length=30,default='')
    like=models.IntegerField(default=0)



class Comment(models.Model):
    writer =  models.ForeignKey(User,on_delete=models.CASCADE,default='')
    context=models.TextField(max_length=100, default='')

