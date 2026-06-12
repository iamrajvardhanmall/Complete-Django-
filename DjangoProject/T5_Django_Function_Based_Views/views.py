from django.shortcuts import render
from .models import raj

def list_view(request):
    # dictionary for intial data with field names as keys
    context = {}
    
    # add the dictionary during intialization
    context["dataset"] = raj.objects.all()
    return render(request, "list_view.html", context)

