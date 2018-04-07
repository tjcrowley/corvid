from django.conf.urls import url
from views import new_channel, ChannelListView
from broadcast.views import on_publish, on_publish_done, subscribe,\
    whitelist_add, WhiteListView, edit_channel, channel

urlpatterns = [
    url(r'^add/', new_channel, name = 'new_channel'),
    url(r'^edit/', edit_channel, {}, 'channel_edit'),
    url(r'^domain/add/', whitelist_add, name = 'new_domain'),
    url(r'^whitelist/', WhiteListView.as_view(), name = 'whitelist_view'),
    url(r'^subscribe/(?P<slug>[\w-]+)/$', subscribe, name = 'subscribe'),
    url(r'^on_publish/', on_publish, name = 'on_publish'),
    url(r'^on_publish_done/', on_publish_done, name = 'on_publish_done'),
    url(r'^$', ChannelListView.as_view(), name='channel-list'),
    url(r'^(?P<slug>[\w-]+)/$', channel, name='channel_detail'),
]
