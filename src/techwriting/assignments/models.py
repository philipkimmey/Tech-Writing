from django.db import models
from django.conf import settings

from techwriting.meetings.models import ClassMeeting, GradingMeeting

def get_file_path(instance, filename):
    extension = filename.split('.')[-1]
    return "%s.%s" % (instance.pk, extension)

class Assignment(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    class_meetings = models.ManyToManyField(ClassMeeting, blank=True)
    grading_meetings = models.ManyToManyField(GradingMeeting, blank=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/assignment/%d/" % self.pk
    
class AssignmentAttachment(models.Model):
    title = models.CharField(max_length=60)
    assignment = models.ForeignKey(Assignment)
    file = models.FileField(upload_to=get_file_path, max_length=200)
    def __unicode__(self):
        return self.title
