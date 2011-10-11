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
    form = SignupForm(request.POST or None)
    next = request.GET.get('next', '/')

    if form.is_valid():
        new_user = form.save()
        user = auth.authenticate(username=new_user.username, password=form.cleaned_data['password1'])
        auth.login(request, user)
        messages.success(request, 'Your account was successfully created')
        return redirect(next)

    return render_to_response('registration/signup.html', {
        'form':form,
        'next':next,
    }, RequestContext(request))


def login(request):
    if request.user.is_authenticated():
        return redirect('/')
    
    form = AuthenticationForm(None, request.POST or None)

    if form.is_valid():
        auth.login(request, form.get_user())
        return redirect(next)
    
    return render_to_response('registration/login.html', {
        'form':form,
        'next':next,
    }, RequestContext(request))

    # if request.method == 'POST':
    #     form = AuthenticationForm(request, request.POST)
    #     if form.is_valid():
    #         print "form.is_valid()"
    #         user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
    #         if user is not None:
    #             print "user is not None"
    #             if user.is_active:
    #                 print "user.is_active"
    #                 auth.login(request, user)
    #                 return redirect(request.GET.get('next','/'))
    #             else:
    #                 pass # send an "inactive" message
    #         else:
    #             pass # send an "error" message
    # else:
    #     form = AuthenticationForm()
    
    # return render_to_response('registration/login.html', {
    #     'form':form,
    # }, RequestContext(request))
