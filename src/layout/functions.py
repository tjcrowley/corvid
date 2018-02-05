from broadcast.models import ChannelDomain

def whitelister(channel, domain):
    whitelist = ChannelDomain.objects.all()
    try:
        listed = whitelist.get(channel=channel)
    except listed.DoesNotExist:
        return True
    try:
        whitelisted = ChannelDomain.objects.filter(channel=channel, domain=domain.lower())
    except whitelisted.DoesNotExist:
        return False
    return True