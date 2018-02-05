from broadcast.models import ChannelDomain

def whitelister(channel, domain):
    try:
        listed = ChannelDomain.objects.filter(channel=channel)
    except ChannelDomain.DoesNotExist:
        return True
    try:
        whitelisted = ChannelDomain.objects.get(channel=channel, domain=domain.lower())
    except ChannelDomain.DoesNotExist:
        return False
    return True