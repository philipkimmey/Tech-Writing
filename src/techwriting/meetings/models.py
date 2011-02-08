from django.db import models

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=50)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    short_description = models.CharField(max_length=60)
    description = models.TextField()

class ClassMeeting(Meeting):
    pass

class GradingMeeting(Meeting):
    pass
