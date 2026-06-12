from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

# create a function-based view
def raj(request):
    # fetch current date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return HttpResponse
    return HttpResponse(html)
