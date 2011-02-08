from django.db import models
from django.conf import settings

from techwriting.meetings.models import Meeting

def get_file_path(instance, filename):
    extension = filename.split('.')[-1]
    return "%s.%s" % (instance.pk, extension)

class Assignment(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    meetings = models.ManyToManyField(Meeting)
    
class Attachment(models.Model):
    title = models.CharField(max_length=60)
    meetings = models.ManyToManyField(Meeting, blank=True)
    assignments = models.ManyToManyField(Assignment, blank=True)
    file = models.FileField(upload_to=get_file_path, max_length=200)
    def __unicode__(self):
        return self.title
