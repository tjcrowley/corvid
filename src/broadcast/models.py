import uuid
from django.db import models
from django.contrib.auth.models import User
#models.py
import os
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from broadcast.functions import createStream


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.slug), filename)

class Channel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    live_at = models.DateTimeField(editable=False,null=True, blank=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=140, unique=True)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stream_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    public = models.BooleanField()
    akamai_stream_id = models.IntegerField(max_length=5, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Channel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    
    def get_stream_id(self):
        if self.akamai_stream_id =="" or self.akamai_stream_id==415:
            result = createStream(self.stream_key)
            if result.status_code == 202:
                self.akamai_stream_id = result.headers.get('location')
            else:
                self.akamai_stream_id = result.status_code
                
    def get_viewers(self):
        return ChannelUser.objects.filter(channel = self).count()
    
    def get_mods(self):
        return ChannelMod.objects.filter(channel = self).count()
    
    def save(self, *args, **kwargs):
        if not self.akamai_stream_id:
            self.get_stream_id()
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Channel,self).save()
        
class ChannelMod(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class ChannelDomain(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    domain = models.CharField(max_length=30)
    
class ChannelUser(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

