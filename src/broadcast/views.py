from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import ChannelForm
from models import Channel
from broadcast.models import ChannelMod

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



class ChannelListView(ListView):
    model = Channel
    
    def dispatch(self, request, *args, **kwargs):
        # check if there is some video onsite
        if request.subdomain:
            return redirect('subdomain')

