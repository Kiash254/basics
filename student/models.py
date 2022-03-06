from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__ (self):
     return f'name{self.name}'

class Room(models.Model):
    host=models.ForeignKey(User , on_delete=models.SET_NULL ,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(max_length=200,null=True,blank=True)
    update=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_created')
    def __str__ (self):
     return f'name{self.name},description{self.description},'

class Meso(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    body=models.TextField()
    update=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return self.body[0:50]