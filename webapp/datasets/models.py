from django.db import models
from webapp.users.models import UserProfile
from tagging.fields import TagField
from tagging.models import Tag

class Dataset(models.Model):
    name = models.CharField(max_length=50, help_text="Name for your dataset")
    description = models.TextField(help_text="Describe the contents of the dataset or any research usage")
    tags = TagField(help_text="Comma or space separated tags to describe this data")
    data = models.FileField(upload_to='data')
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserProfile)
    downloads = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)