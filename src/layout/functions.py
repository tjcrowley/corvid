from broadcast.models import ChannelDomain
from __builtin__ import True
def whitelisted(channel, domain):
    try:
        whitelist = ChannelDomain.objects.filter(channel=channel)
    except whitelist.DoesNotExist:
        return True
    try:
        whitelisted = ChannelDomain.objects.filter(channel=channel, domain=domain.strip())
    except whitelisted.DoesNotExist:
        return False
    return True