from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User

from webapp.datasets.models import Dataset

def view_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None

    datasets = Dataset.objects.filter(user=user).order_by('downloads')

    return render_to_response('users/view_user.html', {
        'user':user,
        'datasets':datasets,
    }, context_instance=RequestContext(request))