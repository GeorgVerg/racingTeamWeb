from django.forms import ModelForm
from .models import ContactInfo, ContactRequest

class ContactInfoForm(ModelForm):
    class Meta:
        model = ContactInfo
        fields = ["firstName", "lastName", "email", ]

        labels = {
            "firstName":"First name",
            "lastName":"Last name",
        }


class ContactRequestForm(ModelForm):
    class Meta:
        model = ContactRequest
        fields = ["requestTitle", "request"]

        labels = {
            "requestTitle":"Inquiry title",
            "request":"Content"
        }
