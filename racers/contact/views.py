from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .forms import ContactRequestForm, ContactInfoForm

# Create your views here.

class indexView(TemplateView):
    template_name = "contact/index.html"

class ourContactInfoView(TemplateView):
    template_name = "contact/ourContactInfo.html"

class createRequestView(FormView):
    template_name = "contact/createRequest.html"
    form_class = ContactInfoForm
    success_url = reverse_lazy("contactUs-thanks")

    # def form_valid(self, form):
        ## form.send_email()
        # return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if"request_form" not in context:
            context["request_form"] = ContactRequestForm()
        return context
    
    def post(self, request, *args, **kwargs):
        contact_form = self.get_form()
        request_form = ContactRequestForm(self.request.POST)

        if contact_form.is_valid() and request_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()

            request_obj = request_form.save(commit=False)
            request_obj.contact_info = contact
            request_obj.save()

            return self.form_valid(contact_form)
        return self.form_invalid(contact_form)


class thanksView(TemplateView):
    template_name = "contact/thanks.html"
    
