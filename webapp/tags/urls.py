from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('datasets.views',
    url(r'^$', 'index'),
    url(r'^(?P<tag_name>[0-9a-z]+)$', 'view_tag'),
)