from typing import Any
from django import http
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)

class PrivacyView(TemplateView):
    template_name = "privacy.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)
