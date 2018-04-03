from django import forms

from services.models import ServiceRequest

class RequestServiceForm(forms.ModelForm):

    class Meta:
        model = ServiceRequest
        fields = ['contact_name', 'email', 'type_of_service', 'message']
