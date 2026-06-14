from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .models import updateRaj
from .forms import updateForm

# after updating it will redirect to detail_View
def detail_view(request, id):
    # dictionary for intial data with
    # field names as keys
    context = {}
    
    # add the dictionary during initialization
    context["data"] = updateRaj.objects.get(id = id)
    
    return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):
    # dictionary for intial data with
    # field names as keys
    context = {}
    
    # fetch the object related to passed id
    obj = get_object_or_404(updateRaj, id = id)
    
    # pass the object as instance in form
    form = updateForm(request.POST or None, instance = obj)
    
    # save the data form the form and
    # redirect to detail_view
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/T5_Update_View_Function_based_Views_Django/" + str(id) + "/")
    
    # add form dictionary to context
    context["form"] = form
    
    return render(request, "update_view.html", context)
    