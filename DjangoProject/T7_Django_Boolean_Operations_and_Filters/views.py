from django.shortcuts import render

# Create your views here.
def boolean_view(request):
    context = {
        "data": 99,
    }
    
    return render(request, 'boolean.html', context)