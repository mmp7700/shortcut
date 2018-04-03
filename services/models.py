from django.db import models

from wagtail.core.models import Page
from wagtail.core.blocks import StreamBlock
from home.blocks import BaseStreamBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

class ServicePage(Page):
    pass


class ServiceDetailPage(Page):
    pass


class ServiceType(models.Model):
    VIDEOS = 'V'
    WEB_SITES = 'W'
    APPS = 'A'

    SERVICE_CHOICES = (
        (VIDEOS, 'Videos'),
        (WEB_SITES, 'Web Sites'),
        (APPS, 'Apps')
    )
    type = models.CharField(
        choices = SERVICE_CHOICES,
        max_length=10
    )

    def __str__(self):
        return self.type

class ServiceRequest(models.Model):
    type_of_service = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    contact_name = models.CharField(blank=True, max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField(blank=True)

    def __str__(self):
        return '%s - %s - %s' % (self.type_of_service, self.email, self.contact_name)
