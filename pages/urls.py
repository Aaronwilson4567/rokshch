#import path to power our url patterns
from django.urls import path
#iport view.py files to look up homePageView Method
from.views import homePageView

urlpatterns=[
    path('',homePageView,name='home'),
]