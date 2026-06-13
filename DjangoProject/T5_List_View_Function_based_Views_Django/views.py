from django.shortcuts import render
from .models import T5_List_view_function_raj

# Create your views here.
# def list_view(request):
#     context = {
#         "dataset": T5_List_view_function_raj.objects.all()
        
#     }
#     return render(request, "list_view.html", context)




# Sorting the List (Descending Order)
# You can order the results in reverse (newest first) by modifying the view:
# def list_view(request):
#     context = {
#         "dataset": T5_List_view_function_raj.objects.all().order_by("-id")
        
#     }
#     return render(request, "list_view.html", context)



# To display only items with the word “title” in their title, update the view:
def list_view(request):
    context = {
        "dataset": T5_List_view_function_raj.objects.filter(title__icontains="title")
    }
    return render(request, "list_view.html", context)