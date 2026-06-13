from django.shortcuts import render

# Create your views here.
from .models import rajModel

# pass id attribute from urls
def detail_view(request, id):
    # dictionary for intial data with field names as keys
    context = {}

    # add the dictionary during intialization
    context["data"] = rajModel.objects.get(id = id)
    return render(request, "detail_view.html", context)
