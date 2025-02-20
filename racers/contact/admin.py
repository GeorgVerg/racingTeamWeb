from django.contrib import admin

from .models import ContactInfo, ContactRequest

# Register your models here.

admin.site.register(ContactInfo)
admin.site.register(ContactRequest)