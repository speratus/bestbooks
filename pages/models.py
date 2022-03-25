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
