from django.db import models
from django.contrib.auth.models import User
#models.py
import os
from django.utils.text import slugify

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Channel(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=140, unique=True)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stream_key = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
 
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Channel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()
    
class ChannelMod(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class ChannelDomain(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    domain = models.CharField(max_length=30)
    
class ChannelUser(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)