from django.shortcuts import render

# Create your views here.
def get_home_view(request):
    print(request.GET)  # Prints the submitted data as a QueryDict
    return render(request, "get_home.html")

def post_home_view(request):
    if request.method == "POST":
        print(request.POST)  # Prints the POSTed data as a QueryDict
        name = request.POST.get('your_name')
    return render(request, "post_home.html")