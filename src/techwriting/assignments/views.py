from django.shortcuts import render_to_response
from django.template import RequestContext

from techwriting.assignments.models import Assignment

def assignment(request, pk=None):
    assignment = Assignment.objects.get(pk=pk)
    return render_to_response('assignment.html', {'assignment': assignment}, context_instance=RequestContext(request))
