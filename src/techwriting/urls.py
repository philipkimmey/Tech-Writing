from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'index.html'}), 
    (r'^syllabus/$', direct_to_template, {'template': 'syllabus.html'}),
    (r'^course/(?P<pk>\d+)/$', 'techwriting.meetings.views.course'),
    (r'^grading/(?P<pk>\d+)/$', 'techwriting.meetings.views.grading'),

    (r'^assignment/(?P<pk>\d+)/$', 'techwriting.assignments.views.assignment'),

    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'}
        ),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}
        ),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    import os
    doc_root = os.path.join(settings.BASE_PATH, 'src', 'static')
    media_root = os.path.join(settings.BASE_PATH, 'media')
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': doc_root}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': media_root}),
        )

