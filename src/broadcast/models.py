from django.db import models
from django.contrib.auth.models import User
#models.py
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Channel(models.Model):
    name = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stream_key = models.TextField(blank=True, null=True)
    
class ChannelMod(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class ChannelDomain(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    domain = models.CharField(max_length=30)
    
class ChannelUser(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)