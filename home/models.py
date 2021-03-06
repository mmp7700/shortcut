from django.db import models

from wagtail.core.models import Page
from wagtail.core.blocks import StreamBlock
from home.blocks import BaseStreamBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

class HomePage(Page):
    body = StreamField(
        BaseStreamBlock(), blank=True
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
