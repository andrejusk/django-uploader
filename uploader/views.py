from django.shortcuts import render
from django.views import generic


class Home(generic.CreateView):
    template_name = 'home.html'