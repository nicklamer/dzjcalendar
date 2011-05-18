from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dzjsite/', include('dzjsite.foo.urls')),
     (r'^dzjcalendar/$', 'dzjcalendar.views.index'),
     (r'^cal$', 'dzjcalendar.views.calendar'),
     (r'^calendar_frame$', 'dzjcalendar.views.calendar_frame'),
     (r'^$', 'dzjcalendar.views.index'),
     (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': '/home/rudy/dzjsite/site_media'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
