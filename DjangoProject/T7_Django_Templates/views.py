from django.shortcuts import render

# Create your views here.
def simple_view(request):
    context = {"data": "Raj is the best"}
    return render(request, "raj.html", context)

def check_age(request):
    age = None
    if request.method == 'POST':
        # request.POST.get returns a string, default to "0"
        age = int(request.POST.get('age', 0))
    return render(request, 'check_age.html', {'age': age})

def loop(request):
    data = "Raj is the Best"
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {
        "data": data,
        "list": number_list
    }
    return render(request, "loop.html", context)
