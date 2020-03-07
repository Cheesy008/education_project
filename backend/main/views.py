from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeTemplate(TemplateView):
    template_name = 'home.html'
