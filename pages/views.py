from django.shortcuts import render


#import http responses to return Http response object to user
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"
    


