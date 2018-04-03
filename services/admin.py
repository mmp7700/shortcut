from django.contrib import admin
from services.models import ServiceType
from services.models import ServiceRequest

class ServicesAdmin(admin.ModelAdmin):
    pass

class ServiceRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServiceType, ServicesAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
