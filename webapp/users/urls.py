from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('webapp.users.views',
    url(r'^(?P<username>[0-9a-z]+)$', 'view_user'),
)