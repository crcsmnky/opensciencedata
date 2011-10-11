from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from local_settings import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'webapp.views.home', name='home'),
    url(r'^about', 'webapp.views.about', name='about'),
    url(r'^contact', 'webapp.views.contact', name='contact'),

    url(r'^users/', include('users.urls')),
    url(r'^datasets/', include('datasets.urls')),
    url(r'^tags/', include('tags.urls')),

    url(r'^login/$', login),
    url(r'^logout/$', logout),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './static'}),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './uploads'}),
)

if DEBUG:
    urlpatterns += patterns(
        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    )
