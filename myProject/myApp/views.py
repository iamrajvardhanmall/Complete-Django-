from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello, this is my first Django app response!")

def myfunctionabout(request):
    return HttpResponse("This is the about page of my first Django app.")
    # Alternatively, you can return a JSON response
    # return JsonResponse({"message": "This is the about page of my first Django app."})

def add(request, a, b):
    return HttpResponse(f"The sum of {a} and {b} is {a + b}.")
# NOTE: If we use x and y instead of a and b, it will give an error because in urls.py we defined <int:a> and <int:b>.

def intro(request, name, age):
    mydictionary = {
        "name": name,
        "age": age,
    }
    return JsonResponse(mydictionary)
# Note: If we use different variable names instead of name and age, it will give an error because in urls.py we defined <str:name> and <int:age>.

def myFirstPage(request):
    return render(request, 'index.html')

def mySecondPage(request):
    return render(request, 'second.html')

def myThirdPage(request):
    var = "Hello, World"
    greeting = "Hello Bhai kya haal chal hai"
    fruits = ["apple", "banana", "cherry"]
    num1, num2 = 5, 10
    ans = num1 > num2
    # print(ans)
    mydictionary = {
        "var": var,
        "msg": greeting,
        "fruits": fruits,
        "num1": num1,
        "num2": num2,
        "ans": ans,
    }
    return render(request, 'third.html', context=mydictionary)

def myimagepage(request):
    return render(request, 'imagepage.html')

def myimagepage2(request):
    return render(request, 'imagepage2.html')

def myimagepage3(request):
    return render(request, 'imagepage3.html')

def myimagepage4(request):
    return render(request, 'imagepage4.html')

def myimagepage5(request, imagename):
    myimagename = imagename
    myimagename = myimagename.lower()
    print(myimagename)
    if myimagename == "django":
        var = True
    elif myimagename == "python":
        var = False
    mydictionary = {
        "var": var
    }
    return render(request, 'imagepage5.html', context=mydictionary)