from django.template import RequestContext
from django.shortcuts import render_to_response

from techwriting.meetings.models import ClassMeeting, GradingMeeting

def course(request, pk=None):
    meeting = ClassMeeting.objects.get(pk=pk) 
    return render_to_response('class.html', {'meeting': meeting}, context_instance=RequestContext(request))

def grading(request, pk=None):
    meeting = GradingMeeting.objects.get(pk=pk)
    return render_to_response('grading.html', {'meeting': meeting}, context_instance=RequestContext(request))
