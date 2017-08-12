from django.contrib import admin
from models import Channel

class ChannelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Channel, ChannelAdmin)