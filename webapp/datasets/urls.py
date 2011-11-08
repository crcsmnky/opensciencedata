from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('webapp.datasets.views',
    url(r'^$', 'index'),
    url(r'^add/$', 'add_dataset'),
    url(r'^user/(?P<username>[0-9a-z]+)/$', 'user_datasets'),
    url(r'^(?P<id>[0-9a-z]+)/view/$', 'view_dataset'),
    url(r'^(?P<id>[0-9a-z]+)/edit/$', 'edit_dataset'),
    url(r'^(?P<id>[0-9a-z]+)/download/$', 'download_dataset'),
)