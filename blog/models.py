from django.db import models
from django.utils.html import format_html
from tinymce import models as tinymce_models
from django.core.urlresolvers import reverse


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
    tags = models.ManyToManyField(Tag)

    objects = EntryQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("entrada", kwargs={"slug": self.slug})

    def body_html(self):
        return format_html(self.body)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
