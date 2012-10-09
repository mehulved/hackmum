# Create your views here.

from hsmreg.models import Event
from hsmreg.models import Users
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404

def index(request):
    event_list = Event.objects.all().order_by('-event_date') 
    return render_to_response('events/index.html', {'event_list': event_list})

def event_detail(request, event_id):
    user_list = get_list_or_404(Users.objects.filter(event_id__exact=event_id))
    return render_to_response('events/event_details.html', {'user_list': user_list, 'event_id': event_id})

def users_detail(request, user_id):
    user_data = get_list_or_404(Users.objects.filter(id=user_id))
    return render_to_response('users/user_details.html', {'user_data': user_data, 'user_id': user_id})

def user_register(request, event_id):
    return render_to_response('users/register.html', {'event_id': event_id})
