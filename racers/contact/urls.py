from django.urls import path

from .views import createRequestView, indexView, ourContactInfoView, thanksView

urlpatterns = [
    path("", indexView.as_view(), name="contactUs-index"),
    path("thanks/", thanksView.as_view(), name="contactUs-thanks"),
    path("create-request/", createRequestView.as_view(), name="contactUs-createRequest"),
    path("our-contact-info/", ourContactInfoView.as_view(), name="contactUs-ourContactInfo")
]
