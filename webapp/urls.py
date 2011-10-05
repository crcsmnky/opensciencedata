from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(
    url(r'^$', 'webapp.views.home', name='home'),
    url(r'^users/', include('webapp.users.urls')),
    url(r'^datasets/', include('webapp.users.urls')),
    url(r'^tags/', include('webapp.users.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    )
