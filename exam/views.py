from django.shortcuts import render
from django.views import generic

class MainView(generic.TemplateView):
    """View used to show reports of repair requests
    """
    template_name = '../templates/exam/main.html'
