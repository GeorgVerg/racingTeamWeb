from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ContactInfo(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):  
        return self.firstName + " " + self.lastName   

class ContactRequest(models.Model):

    class ReasonForRequest(models.TextChoices):
        QUESTION = "For a question", _("Question")
        COLLABORATION = "For a collaboration", _("Collaboration")
        SPONSORSHIP = "For a sponsorship", _("Sponsorship")
        OTHER = "For another reason", _("Other")


    requestTitle = models.CharField(max_length=150)
    request = models.TextField()
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)
    reason_for_the_inquiry = models.CharField(
        max_length=20,
        choices=ReasonForRequest.choices,
        default=ReasonForRequest.OTHER,
    )

    def __str__(self):
        return self.requestTitle