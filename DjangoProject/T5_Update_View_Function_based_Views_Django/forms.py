from django import forms
from .models import updateRaj

# Creating a form
class updateForm(forms.ModelForm):
    
    # create Meta Class
    class Meta:
        model = updateRaj
        
        # specify feilds to be used
        fields = [
            "title",
            "description"
        ]