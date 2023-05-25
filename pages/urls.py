#import path to power our url patterns
from django.urls import path
#iport view.py files to look up homePageView Method
from pages.views import HomePageView,AboutPageView

urlpatterns=[
    path("",HomePageView.as_view(),name="home"),
    path("about/",AboutPageView.as_view(),name="about")
]