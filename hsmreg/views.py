# Create your views here.

from hsmreg.models import Event
from hsmreg.models import Users
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, render
from django import forms
from django.db import models
from django.http import HttpResponseRedirect
from django.template import RequestContext

class RegisterForm(forms.Form):
    fullname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    twitter = forms.CharField(max_length=20)
    facebook = forms.CharField(max_length=20)
    github = forms.CharField(max_length=20)
    geeklist = forms.CharField(max_length=20)

def index(request):
    event_list = Event.objects.all().order_by('-event_date') 
    return render_to_response('events_index.html', {'event_list': event_list}, context_instance = RequestContext(request))

def event_detail(request, event_id):
    user_list = Users.objects.filter(event_id__exact=event_id)
    return render_to_response('event_details.html', {'user_list': user_list, 'event_id': event_id})

def users_detail(request, user_id, event_id):
    user_data = get_list_or_404(Users.objects.filter(id=user_id).filter(event_id=event_id))
    return render_to_response('user_details.html', {'user_data': user_data, 'user_id': user_id})

def user_register(request, event_id):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            twitter = form.cleaned_data['twitter']
            facebook = form.cleaned_data['facebook']
            github = form.cleaned_data['github']
            geeklist = form.cleaned_data['geeklist']
            u = Users.objects.create(event_id=event_id,fullname=fullname, email=email, twitter=twitter, facebook=facebook, github=github, geeklist=geeklist)
            return HttpResponseRedirect('/event/%s' % event_id)
    else:
        form = RegisterForm()
    return render(request,'user_register.html', {'event_id': event_id, 'form': form})
