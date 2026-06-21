from django.shortcuts import render

# Create your views here.
def if_view(request):
    context = {
        # "data": 0,   # 0 means Data is Empty
        # "data": False,   # False means Empty
        "data": 99,
    }
    return render(request, 'if.html', context)