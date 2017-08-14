from django.conf.urls import include, url
from views import new_channel, ChannelListView
from broadcast.views import on_publish, on_publish_done

urlpatterns = [
    url(r'^$', ChannelListView.as_view(), name='channel-list'),
    url(r'^add/', new_channel, name = 'new_channel'),
    url(r'^on_publish/', on_publish, name = 'on_publish'),
    url(r'^on_publish_done/', on_publish_done, name = 'on_publish_done'),
    ]
