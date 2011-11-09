from django.conf.urls.defaults import patterns, include, url

from webapp.datasets.feed import DatasetFeed

urlpatterns = patterns('webapp.datasets.views',
    (r'^$', 'index'),
    (r'^add/$', 'add_dataset'),
    (r'^feed/$', DatasetFeed()),
    (r'^user/(?P<username>[0-9a-z]+)/$', 'user_datasets'),
    (r'^(?P<id>[0-9a-z]+)/view/$', 'view_dataset'),
    (r'^(?P<id>[0-9a-z]+)/edit/$', 'edit_dataset'),
    (r'^(?P<id>[0-9a-z]+)/download/$', 'download_dataset'),
)