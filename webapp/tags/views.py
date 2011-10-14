from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from tagging.models import Tag, TaggedItem

from webapp.datasets.models import Dataset

def index(request):
    tags = Tag.objects.usage_for_model(Dataset, counts=True)
    return render_to_response('tags/index.html', {
        'tags':tags,
    }, context_instance=RequestContext(request))

def view_tag(request, tag_name):
    datasets = TaggedItem.objects.get_by_model(Dataset, tag_name)
    return render_to_response('tags/view_tag.html', {
        'tag_name':tag_name,
        'datasets':datasets,
    }, context_instance=RequestContext(request))
    