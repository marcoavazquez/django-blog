from django.db import models
from tinymce import models as tinymce_models

class EntryQuerySet(models.QuerySet):

    def published(self):
        return self.filter(publish=True)


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.slug


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = tinymce_models.HTMLField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = EntryQuerySet.as_manager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
