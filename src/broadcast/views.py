from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from .forms import ChannelForm
from models import Channel
from broadcast.models import ChannelMod, ChannelUser, ChannelDomain
from django.contrib.auth.decorators import login_required
from broadcast.forms import WhitelistForm

@login_required
def new_channel(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ChannelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            channel = form.save(commit=False)
            mod = ChannelMod()
            channel.save()
            mod.channel = channel
            mod.user = request.user
            mod.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/channel/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ChannelForm()

    return render(request, 'forms/form.html', {'form': form})


@login_required
def edit_channel(request, slug):
    channel = get_object_or_404(Channel, slug=slug)
    if ChannelMod.objects.filter(channel=channel, user=request.user).exists() or ChannelUser.objects.filter(channel=channel,user=request.user).exists():
        channel_allowed= True
    else:
            return HttpResponseForbidden()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ChannelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            channel = form.save(commit=False)
            mod = ChannelMod()
            channel.save()
            mod.channel = channel
            mod.user = request.user
            mod.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/channel/')



    # if a GET (or any other method) we'll create a blank form
    else:
        form = ChannelForm()

    return render(request, 'forms/form.html', {'form': form})



class ChannelListView(ListView):
    model = Channel
    


class WhiteListView(ListView):
    model = ChannelDomain
    

@require_POST
def on_publish(request):
    # nginx-rtmp makes the stream name available in the POST body via `name`
    # import the logging library
    #import logging
    
    # Get an instance of a logger
    stream_key = request.POST['name']
    # Assuming we have a model `Stream` with a foreign key
    # to `django.contrib.auth.models.User`, we can
    # lookup the stream and verify the publisher is allowed to stream.
    stream = get_object_or_404(Channel, stream_key=stream_key)

    # You can ban streamers by setting them inactive.
    if not stream:
        return HttpResponseForbidden("inactive channel")

    # Set the stream live
    stream.live_at = timezone.now()
    stream.save()

    # Redirect the private stream key to the user's public stream
    # NOTE: a relative redirect like this will not work in
    #       Django <= 1.8
    return HttpResponseRedirect(stream.slug)


@require_POST
def on_publish_done(request):
    # When a stream stops nginx-rtmp will still dispatch callbacks
    # using the original stream key, not the redirected stream name.
    stream_key = request.POST['name']

    # Set the stream offline
    Channel.objects.filter(stream_key=stream_key).update(live_at=None)

    # Response is ignored.
    return HttpResponse("OK")


@login_required
def subscribe(request):
    """ Default view for the root """
    if request.subdomain:
        channel = get_object_or_404(Channel,slug=request.subdomain)
        subscription, created = ChannelUser.objects.get_or_create(user=request.user, channel = channel)
        return HttpResponseRedirect('/channel/')
    else:
        return HttpResponseRedirect('/')


@login_required
def whitelist_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WhitelistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            domain = form.save(commit=False)
            channel = Channel
            domain.channel = get_object_or_404(Channel,slug=request.subdomain)
            domain.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/channel/whitelist/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WhitelistForm()

    return render(request, 'forms/form.html', {'form': form})

