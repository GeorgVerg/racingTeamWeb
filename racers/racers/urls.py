"""
URL configuration for racers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import index, set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index.as_view(), name="index"),
    path("set-language/", set_language, name="set_language"),

    path("contact-us/", include("contact.urls")),
    path("about/", include("about.urls")),
    path("goal/", include("goal.urls")),
    path("competition", include("competition.urls")),
    path("sponsorships", include("sponsorships.urls")),
]
