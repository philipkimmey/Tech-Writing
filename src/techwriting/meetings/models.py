from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    start = models.DateTimeField()
    finish = models.DateTimeField()

class ClassMeeting(Meeting):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=60)
    description = models.TextField()
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/course/%s/" % self.pk

class GradingMeeting(Meeting):
    user = models.ForeignKey(User, null=True, blank=True)
    def __unicode__(self):
        return self.title
