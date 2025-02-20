from django.forms import ModelForm
from .models import ContactInfo, ContactRequest

class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        fields = ["firstName", "lastName", "email", ]


class ContactRequestForm(ModelForm):
    class Meta:
        model = ContactRequest
        fields = ["requestTitle", "request"]
