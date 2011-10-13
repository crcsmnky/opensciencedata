from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'webapp.views.home'),
    (r'^about', 'webapp.views.about'),
    (r'^contact', 'webapp.views.contact'),
    (r'^signup', 'webapp.views.signup'),

    (r'^users/', include('users.urls')),
    (r'^datasets/', include('datasets.urls')),
    (r'^tags/', include('tags.urls')),

    # (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^login/$', 'webapp.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './static'}),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './uploads'}),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        # Uncomment the next line to enable the admin:
        (r'^admin/', include(admin.site.urls)),
    )