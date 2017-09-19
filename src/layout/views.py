""" Views for the layout application """

from django.shortcuts import render, render_to_response, HttpResponseRedirect,\
    get_object_or_404
import django
from broadcast.models import Channel, ChannelMod, ChannelUser
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def home(request):
    """ Default view for the root """
    djangoversion = django.get_version()
    if request.subdomain:
        channel = get_object_or_404(Channel,slug=request.subdomain)
        if request.user.is_authenticated():
            if ChannelMod.objects.filter(channel=channel, user=request.user).exists() or ChannelUser.objects.filter(channel=channel,user=request.user).exists():
                channel_allowed=True
            else:
                channel_allowed = False
        else:
            channel_allowed = False
        return render(request, 'broadcast/channel.html',{'djangoversion':djangoversion,'channel':channel ,'channel_allowed':channel_allowed })
    else:
        channels = Channel.objects.all()
        
        return render(request, 'layout/home.html',{'djangoversion':djangoversion, 'channels':channels })

def profile(request):
    return  render(request, "user/profile.html" )    
