from datetime import datetime

from techwriting.meetings.models import ClassMeeting, GradingMeeting
from techwriting.assignments.models import Assignment

def course_meetings(request):
    course_meetings = ClassMeeting.objects.filter(finish__gt=datetime.now()).order_by('finish')[:3]
    return {'course_meetings': course_meetings}

def grading_meetings(request):
    grading_meetings = GradingMeeting.objects.filter(user=request.user).filter(finish__gt=datetime.now()).order_by('finish')[:3]
    return {'grading_meetings': grading_meetings}

def assignments(request):
    assignments = Assignment.objects.all()
    return {'assignments': assignments}
