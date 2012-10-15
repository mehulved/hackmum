from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackmum.views.home', name='home'),
    # url(r'^hackmum/', include('hackmum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # User Views
    url(r'^$', 'hsmreg.views.index'),
    url(r'^event/(?P<event_id>\d+)/$', 'hsmreg.views.event_detail'),
    url(r'^event/(?P<event_id>\d+)/user/register/$','hsmreg.views.user_register'),
    url(r'^event/(?P<event_id>\d+)/user/(?P<user_id>\d+)/$','hsmreg.views.users_detail'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^about/$', 'hsmreg.views.about'),
)
