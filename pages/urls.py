#import path to power our url patterns
from django.urls import path
#iport view.py files to look up homePageView Method
from pages.views import HomePageView,AboutPageView,DetailView,CreateViewPost,UpdateViewPost,DeleteViewPost

urlpatterns=[
    path("",HomePageView.as_view(),name="home"),
    path("about/",AboutPageView.as_view(),name="about"),
    path("post/<int:pk>/",DetailView.as_view(),name='post_details'),
    path("post/new",CreateViewPost.as_view(),name="post_new"),
    path("post/<int:pk>/edit",UpdateViewPost.as_view(),name="post_edit"),
    path("post/<int:pk>/delete",DeleteViewPost.as_view(),name="post_delete"),

]