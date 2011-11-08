from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from webapp.datasets.models import Dataset

def home(request):
    recent_datasets = Dataset.objects.order_by('updated')[:10]
    top_datasets = Dataset.objects.order_by('downloads')[:10]
    return render_to_response('home.html',{
        'top_datasets': top_datasets,
        'recent_datasets': recent_datasets,
        },RequestContext(request)
    )


def about(request):
    return render_to_response('about.html', {},
        RequestContext(request))


def contact(request):
    return render_to_response('contact.html', {},
        RequestContext(request))
