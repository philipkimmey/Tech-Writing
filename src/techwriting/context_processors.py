from datetime import datetime

from techwriting.meetings.models import ClassMeeting, GradingMeeting

def course_meetings(request):
    course_meetings = ClassMeeting.objects.filter(finish__gt=datetime.now()).order_by('finish')[:3]
    return {'course_meetings': course_meetings}

def assignment_meetings(request):
    return {}
