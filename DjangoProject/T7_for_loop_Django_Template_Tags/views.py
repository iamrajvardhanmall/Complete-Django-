from django.shortcuts import render

# Create your views here.
def raj_view(request):
    # create a dictionary
    context = {
        "data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
    
    return render(request, "for_loop.html", context)