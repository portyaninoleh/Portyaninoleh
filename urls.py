from django.conf.urls.defaults import patterns, include, url
from mysite.views import hello, currentTime, hoursAhead, currentTimeTemplate, timeRender, get_request, athlets, search,  contact
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^time/$', currentTime),
    (r'^time/(\d{1,2})/$', hoursAhead),
    ('^timeTemplate/$', currentTimeTemplate),
    ('^timeRender/$', timeRender),
    ('^get_request/$', get_request),
    ('^athlet/$', athlets),
    (r'^search/$', search),
    (r'^contact_us/$', contact),
)
