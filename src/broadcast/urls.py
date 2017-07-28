from django.conf.urls import include, url
from views import new_channel, ChannelListView

urlpatterns = [
    url(r'^$', ChannelListView.as_view(), name='channel-list'),
    url(r'^add/', new_channel, name = 'new_channel'),
    ]
