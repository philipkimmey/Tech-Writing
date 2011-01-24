from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'index.html'}), 
    (r'^syllabus/$', direct_to_template, {'template': 'syllabus.html'}),
    # Example:
    # (r'^techwriting/', include('techwriting.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    import os
    doc_root = os.path.join(settings.BASE_PATH, 'src', 'static')
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': doc_root}),
        )

