""" Views for the layout application """
from django.contrib.staticfiles import finders
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render, render_to_response, HttpResponseRedirect,\
    get_object_or_404
import django
from broadcast.models import Channel, ChannelMod, ChannelUser
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from layout.functions import whitelisted


@xframe_options_exempt
def home(request):
    """ Default view for the root """
    djangoversion = django.get_version()
    if request.subdomain:
        channel = get_object_or_404(Channel,slug=request.subdomain)
        result = finders.find('live/{{channel.stream_key}}/index.m3u8')
        whitelist = True
        if request.user.is_authenticated():
            if ChannelMod.objects.filter(channel=channel, user=request.user).exists() or ChannelUser.objects.filter(channel=channel,user=request.user).exists():
                channel_allowed = True
              
            else:
                domain = request.user.email.split('@')[1]
                whitelist=whitelisted(channel,domain)
                channel_allowed = False
        else:
            channel_allowed = False
        return render(request, 'broadcast/channel.html',{'djangoversion':djangoversion,'channel':channel ,'channel_allowed':channel_allowed,'whitelist':whitelist,'stream_url': result })
    else:
        channels = Channel.objects.all()
        
        return render(request, 'layout/home.html',{'djangoversion':djangoversion, 'channels':channels })

def profile(request):

    try:
        channels = ChannelMod.objects.filter(user=request.user)
    except ObjectDoesNotExist:
        channels = None
    return  render(request, "user/profile.html",{'channels':channels } )    
