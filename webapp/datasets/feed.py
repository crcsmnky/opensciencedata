from django.contrib.syndication.views import Feed

from webapp.datasets.models import Dataset

class DatasetFeed(Feed):
    title = "open science data datasets"
    link = "/datasets/feed/recent/"
    description = "A feed of the most recently uploaded datasets on opensciencedata.org"

    def items(self):
        return Dataset.objects.order_by('updated')[0:10]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description

