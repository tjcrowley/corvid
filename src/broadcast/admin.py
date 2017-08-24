from django.contrib import admin
from broadcast.models import Channel, ChannelUser, ChannelMod

admin.site.register(Channel)

admin.site.register(ChannelMod)

admin.site.register(ChannelUser)