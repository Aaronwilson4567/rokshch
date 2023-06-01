from django.shortcuts import render


#import http responses to return Http response object to user
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView
from .models import Post
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class HomePageView(ListView):
    model=Post
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class DetailView(DetailView):
    model=Post
    template_name="post_details.html"

class CreateViewPost(CreateView):
    model=Post
    template_name="post_new.html"
    fields=["title","author","body"]

class UpdateViewPost(UpdateView):
    model=Post
    template_name="post_edit.html"
    fields=["title","body"]

class DeleteViewPost(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url=reverse_lazy("home")
    

       
    


