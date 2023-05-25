from django.shortcuts import render


#import http responses to return Http response object to user
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    #retrun http response to user
    return HttpResponse('Hello Django nice to meet you')



