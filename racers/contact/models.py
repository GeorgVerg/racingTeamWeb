from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):  
        return self.firstName + " " + self.lastName   

class ContactRequest(models.Model):
    requestTitle = models.CharField(max_length=150)
    request = models.TextField()
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.requestTitle