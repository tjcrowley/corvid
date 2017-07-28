from django.forms import ModelForm
from models import Channel
# Create the form class.
class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = ['name', 'profile_image', 'description']