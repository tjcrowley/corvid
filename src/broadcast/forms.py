from django.forms import ModelForm
from models import Channel
from broadcast.models import ChannelDomain
# Create the form class.
class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'profile_image', 'description']
        
        

class WhitelistForm(ModelForm):
    class Meta:
        model = ChannelDomain
        fields = ['domain']