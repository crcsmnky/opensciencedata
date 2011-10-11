from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('datasets.views',
    url(r'^$', 'index'),
    url(r'^new/$', 'new_user'),
    url(r'^(?P<username>[0-9a-z]+)$', 'view_user'),
)