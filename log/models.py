from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10,default='')
    nickname = models.CharField(max_length=10,primary_key=True)
    password =models.CharField(max_length=20,default='')
    profile = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    Member =models.CharField(max_length=10,default='')

class Post(models.Model):
    title = models.CharField(max_length=30,default='',null=True)
    # writer =  models.ForeignKey(User ,on_delete=models.CASCADE,default='',null=True) 
    writer= models.CharField(max_length=10, default='')
    content = models.TextField(default='',null=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,null=True)
    date = models.DateTimeField(default='',null=True)
    firstPlace = models.CharField(max_length=30,default='',null=True)
    like=models.IntegerField(default=0,null=True)


# class Comment(models.Model):
#     post=models.ForeignKey(Post ,on_delete=models.CASCADE,default='')
#     writer =  models.ForeignKey(User,on_delete=models.CASCADE,default='')
#     context=models.TextField(max_length=100, default='')


# class PloggingComment(models.Model):
#     post=models.ForeignKey(Plogging ,on_delete=models.CASCADE,default='')
#     writer =  models.ForeignKey(User,on_delete=models.CASCADE,default='')
#     context=models.TextField(max_length=100, default='')