from django.shortcuts import render
from http import HttpResponse

# Create your views here.
def bookingData(request):
    return HttpResponse("hello floks")
