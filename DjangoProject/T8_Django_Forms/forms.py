from django import forms 
from django.core.validators import MinLengthValidator

# Creating a Simple Django Form
class InputForm(forms.Form):
    first_name = forms.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)]
    )
    
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll number")
    pasward = forms.CharField(widget=forms.PasswordInput())
    
    
    
# Create Django Form from Models
# from .models import formModel

# class form_model(forms.ModelForm):
#     class Meta:
#         model = formModel
#         fields = '__all__'