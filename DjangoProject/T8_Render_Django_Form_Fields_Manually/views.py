from django.shortcuts import render

# Create your views here.
from .forms import Inputform


def home_view(request):
    context={}
    context['form'] = Inputform()
    return render(request, 'Inputform.html', context)