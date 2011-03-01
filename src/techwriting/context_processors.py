from datetime import datetime

from techwriting.meetings.models import ClassMeeting, GradingMeeting
from techwriting.assignments.models import Assignment

def course_meetings(request):
    course_meetings = ClassMeeting.objects.filter(finish__gt=datetime.now()).order_by('finish')[:3]
    return {'course_meetings': course_meetings}

def assignment_meetings(request):
    return {}

def assignments(request):
    assignments = Assignment.objects.all()
    return {'assignments': assignments}
