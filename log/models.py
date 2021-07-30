from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10,default='')
    nickname = models.CharField(max_length=10,primary_key=True)
    password =models.CharField(max_length=30,default='')
    profile = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, blank=True, null=True)
    Member =models.CharField(max_length=10,default='')

class Post(models.Model):
    kinds=models.CharField(max_length=7, default='')
    title = models.CharField(max_length=30,default='',null=True)
    writer= models.CharField(max_length=10, default='')
    content = models.TextField(default='',null=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,null=True)
    date = models.DateTimeField(default='',null=True)
    firstPlace = models.CharField(max_length=30,default='',null=True)
    like=models.IntegerField(default=0,null=True)
    like_users= models.ManyToManyField(User)
