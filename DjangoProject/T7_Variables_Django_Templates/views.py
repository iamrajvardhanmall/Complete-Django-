from django.shortcuts import render

# Create your views here.
def raj_view(request):
    context = {
        "first_name": "Rajvardhan",
        "last_name": "Mall",
    }
    return render(request, "raj_view.html", context)