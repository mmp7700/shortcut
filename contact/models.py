from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page


class ContactPage(Page):

    def serve(self, request):
        from services.forms import RequestServiceForm

        if request.method == 'POST':
            form = RequestServiceForm(request.POST)
            if form.is_valid():
                serviceRequest = form.save()
                return render(request, 'contact/contact_page_landing.html', {
                    'page': self,
                    'serviceRequest': serviceRequest,
                })
            else:
                print('FAILed')
        else:
            form = RequestServiceForm()

        return render(request, 'contact/contact_page.html', {
            'page': self,
            'form': form,
        })
