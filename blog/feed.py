from django.contrib.syndication.views import Feed
from .models import Entry


class LatestPosts(Feed):
    title = "M Blog"
    link = "/feed/"
    description = "Latest Post of M"

    def items(self):
        return Entry.objects.published()[:5]
