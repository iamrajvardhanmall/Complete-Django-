from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def root(request):
    return HttpResponse("Welcome to the Root App!")
