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
        channelmod = ChannelMod(user=request.user, channel = channel)
        channeluser = ChannelUser(user=request.user, channel=channel)        
        return render(request, 'broadcast/channel.html',{'djangoversion':djangoversion,'channel':channel ,'channelmod':channelmod ,'channeluser':channeluser })
    else:
        return render(request, 'layout/home.html',{'djangoversion':djangoversion })

def profile(request):
    return  render(request, "user/profile.html" )    
