from django.shortcuts import render
from .models import raj
from .forms import raj_form

# Create your views here.
def create_view(request):
    context = {}
    
    form = raj_form(request.POST or None)
    if form.is_valid():
        form.save()
        
    context['form'] = form
    return render(request, "create_view.html", context)