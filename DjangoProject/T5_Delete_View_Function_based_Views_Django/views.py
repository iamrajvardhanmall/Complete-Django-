from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .models import deleteModel
# Create your views here.

def list_view(request):
    # fetch all objects
    obj = deleteModel.objects.all()
    context = {'obj': obj}
    return render(request, "list.html", context)

def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
    
    # fetch the object related to passed id
    obj = get_object_or_404(deleteModel, id = id)
    
    if request.method == "POST":
        # delete object
        obj.delete()
        
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/T5_Delete_View_Function_based_Views_Django/")
    
    context['obj'] = obj
    return render(request, "delete_view.html", context)

