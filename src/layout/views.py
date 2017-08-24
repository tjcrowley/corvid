""" Views for the layout application """

from django.shortcuts import render, render_to_response, HttpResponseRedirect,\
    get_object_or_404
import django
from broadcast.models import Channel, ChannelMod, ChannelUser

def home(request):
    """ Default view for the root """
    djangoversion = django.get_version()
    if request.subdomain:
        channel = get_object_or_404(Channel,slug=request.subdomain)
        if request.user.is_authenticated():
            channelmod = ChannelMod.objects.get(channel=channel)
            channeluser = ChannelUser.objects.get(channel=channel)
            if channelmod.filter(user=request.user).exists() or channeluser.filter(user=request.user).exists():
                channel_allowed=True
            else:
                channel_allowed = False
        else:
            channel_allowed = False
        return render(request, 'broadcast/channel.html',{'djangoversion':djangoversion,'channel':channel ,'channel_allowed':channel_allowed })
    else:
        return render(request, 'layout/home.html',{'djangoversion':djangoversion })

def profile(request):
    return  render(request, "user/profile.html" )    
