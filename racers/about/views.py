from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy

from .models import About

# Create your views here.
class IndexView(TemplateView):
    template_name = "about/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        return context


class AboutView(DetailView):
    model = About
    context_object_name = "about"

class CreateAboutView(CreateView):
    template_name = "about/createAbout.html"
    model = About
    success_url = reverse_lazy("about-confirm")

    fields = ["text"]
    

class EditAboutView(UpdateView):
    template_name = "about/updateAbout.html"
    model = About
    fields = [
        "text"
    ]
    success_url = reverse_lazy("about-confirm")

class ConfirmationView(TemplateView):
    template_name = "about/confirm.html"
