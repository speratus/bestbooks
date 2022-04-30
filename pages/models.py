from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class StaticPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname='full title')),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('block', blocks.BlockQuoteBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]


class AverageReadingWpm(models.Model):

    reading_time = models.IntegerField(default=238)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(AverageReadingWpm, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return f"Average Words Per Minute: {self.reading_time}"
