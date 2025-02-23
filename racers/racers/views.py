from django.views.generic import TemplateView
from django.utils.translation import activate
from django.shortcuts import redirect

class index(TemplateView):
    template_name = "index.html"

def set_language(request):
    lang_code = request.GET.get("language", "en")
    activate(lang_code)
    response = redirect(request.META.get("HTTP_REFERER", "/"))
    response.set_cookie("django_language", lang_code)
    return response