# Render simple text
from django.http import HttpResponse

def home(Request):
    return HttpResponse("<h1>This is the Django Project</h1>")