from django.conf.urls import patterns, url
from .views import BlogIndexView, BlogDetailView
from .feed import LatestPosts

urlpatterns = patterns('',
    url(r'^feed/$', LatestPosts(), name="feed"),
    url(r'^$', BlogIndexView.as_view(), name="index"),
    url(r'^(?P<slug>\S+)$', BlogDetailView.as_view(), name="entrada"),
)
