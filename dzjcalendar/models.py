from django.db import models

# Create your models here.
class User(models.Model):
    name    = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email   = models.CharField(max_length=50)
    phone   = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s %s (%s)' %(self.name, self.surname, self.email)

class Event(models.Model):
    title      = models.CharField(max_length=50)
    content    = models.CharField(max_length=50)
    where      = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time   = models.DateTimeField()

    def __unicode__(self):
        return 'title:  %s\n content: %s (%s)' %(self.title, self.content)
