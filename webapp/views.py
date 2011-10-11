from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib import messages

from datasets.models import Dataset
from users.forms import SignupForm

def home(request):
    datasets = Dataset.objects.order_by('updated')[:10]
    return render_to_response('home.html',{
        'datasets': datasets,
        },RequestContext(request)
    )


def about(request):
    return render_to_response('about.html', {},
        RequestContext(request))


def contact(request):
    return render_to_response('contact.html', {},
        RequestContext(request))


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.authenticate(username=user.username, password=user.password)
            auth.login(request, user)
            messages.success(request, 'Your account was successfully created')
            redirect(request.GET.get('next','/'))
    else:
        form = SignupForm()

    return render_to_response('registration/signup.html', {
        'form':form,
        }, RequestContext(request))


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    redirect(request.GET.get('next','/'))
                else:
                    pass # send an "inactive" message
            else:
                pass # send an "error" message
    else:
        form = AuthenticationForm()
    
    return render_to_response('registration/login.html', {
        'form':form,
        }, RequestContext(request))
