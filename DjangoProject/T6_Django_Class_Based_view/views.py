from django.shortcuts import render
from django.views.generic import ListView
from .models import rajClass
# Create your views here.

class rajClassView(ListView):
    model = rajClass
    template_name = 'rajClass_list.html'  # template path
    context_object_name = "object_list"  # list name in template