from django.contrib import admin
from broadcast.models import Channel, ChannelUser, ChannelMod, ChannelDomain

admin.site.register(Channel)

admin.site.register(ChannelMod)

admin.site.register(ChannelUser)

admin.site.register(ChannelDomain)
