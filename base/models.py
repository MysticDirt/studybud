from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # sets topic to null if topic is deleted
    name = models.CharField(max_length=200) # text field/string
    description = models.TextField(null=True, blank=True) # null=True means it can be blank, blank=True means the form can be blank
    participants = models.ManyToManyField(User, related_name='participants') # need related name since we already have a User object
    updated = models.DateTimeField(auto_now=True) # takes a time automatically on every save
    created = models.DateTimeField(auto_now_add=True) # takes a time automatically only when it is first created

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # when parent is deleted, delete all the messages
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # takes a time automatically on every save
    created = models.DateTimeField(auto_now_add=True) # takes a time automatically only when it is first created

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]