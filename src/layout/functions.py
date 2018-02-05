from broadcast.models import ChannelDomain
from __builtin__ import True
def whitelisted(channel, domain):
    permitted = False
    try:
        whitelist = ChannelDomain.objects.filter(channel=channel)
    except whitelist.DoesNotExist:
        return True
    try:
        whitelisted = ChannelDomain.objects.filter(channel=channel, domain=domain)
    except whitelisted.DoesNotExist:
        permitted = False
    return permitted