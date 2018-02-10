from django.forms import ModelForm
from models import Channel
from broadcast.models import ChannelDomain
from django.db.models.fields import TextField
from django.forms.fields import CharField
from django.forms.widgets import Textarea
# Create the form class.
class ChannelForm(ModelForm):
    snippet = CharField(required=False,widget=Textarea())
    class Meta:
        model = Channel
        fields = ['name', 'profile_image', 'description','snippet','background','public']
        
        

class WhitelistForm(ModelForm):
    class Meta:
        model = ChannelDomain
        fields = ['domain']
