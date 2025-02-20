from django.urls import path

from .views import IndexView, CreateAboutView, EditAboutView, ConfirmationView

urlpatterns = [
    path("", IndexView.as_view(), name="about-index"),
    path("create/", CreateAboutView.as_view(), name="about-create"),
    path("confirmation/", ConfirmationView.as_view(), name="about-confirm"),
    path("edit/<pk>/", EditAboutView.as_view(), name="about-edit")
]
