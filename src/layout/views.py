""" Views for the layout application """
from django.contrib.staticfiles import finders
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render, render_to_response, HttpResponseRedirect,\
    get_object_or_404
import django
from broadcast.models import Channel, ChannelMod, ChannelUser
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required

from layout.functions import whitelister


@xframe_options_exempt
def home(request):
    """ Default view for the root """
    djangoversion = django.get_version()
    channels = Channel.objects.all()
    return render(request, 'layout/home.html',{'djangoversion':djangoversion, 'channels':channels })

@login_required
def profile(request):

    try:
        channels = ChannelMod.objects.filter(user=request.user)
    except ObjectDoesNotExist:
        channels = None
    return  render(request, "user/profile.html",{'channels':channels } )    
