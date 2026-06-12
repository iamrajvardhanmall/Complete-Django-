from django import forms
from .models import raj

class raj_form(forms.ModelForm):
    class Meta:
        model = raj
        fields = [
            "title",
            "description",
        ]