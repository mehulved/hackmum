from django.db import models

# Create your models here.

class Event(models.Model):
    event_date = models.DateField()
    name = models.CharField(max_length=50)

class Users(models.Model):
    event = models.ForeignKey(Event)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    twitter = models.CharField(max_length=20)
    facebook = models.CharField(max_length=20)
    github = models.CharField(max_length=20)
    geeklist = models.CharField(max_length=20)

