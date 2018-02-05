from broadcast.models import ChannelDomain
from __builtin__ import True
def whitelisted(channel, domain):
    try:
        whitelist = ChannelDomain.objects.filter(channel=channel)
    except whitelist.DoesNotExist:
        allowed = True
    try:
        whitelisted = ChannelDomain.objects.filter(channel=channel, domain=domain)
    except whitelisted.DoesNotExist:
        allowed = False
    return allowed