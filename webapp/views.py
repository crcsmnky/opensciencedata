from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from datasets.models import Dataset

def home(request):
    datasets = Dataset.objects.order_by('updated')[:10]
    return render_to_response(
        'home.html',
        {'datasets': datasets},
        RequestContext(request)
    )

def about(request):
    return render_to_response('about.html', {},
        RequestContext(request))

def contact(request):
    return render_to_response('contact.html', {},
        RequestContext(request))