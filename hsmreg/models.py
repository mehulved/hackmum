from django.db import models

# Create your models here.

class Event(models.Model):
    event_date = models.DateField()
    name = models.CharField(max_length=50)
    active = models.BooleanField()

    def __unicode__(self):
        return u'%s' % (self.name)

class Users(models.Model):
    event = models.ForeignKey(Event)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15, null=True, blank=True, default='')
    twitter = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.CharField(max_length=20, null=True, blank=True)
    github = models.CharField(max_length=20, null=False, blank=False)
    geeklist = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.fullname)
