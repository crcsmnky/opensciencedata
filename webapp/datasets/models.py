from django.db import models
from django.contrib.auth.models import User
import tagging

class Dataset(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    data = models.FileField(upload_to='data/%Y/%m/%d')
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    downloads = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

try:
    tagging.register(Dataset)
except tagging.AlreadyRegistered:
    pass