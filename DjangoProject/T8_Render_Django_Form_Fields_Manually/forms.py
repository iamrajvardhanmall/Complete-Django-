from django import forms

# Creating form
class Inputform(forms.Form):
    first_name = forms.CharField(max_length= 200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())
    
    # NOTE:
    # The left side (e.g., first_name) is the name of the form field. 
    # The right side defines the type of field and its attributes (e.g., CharField, IntegerField, widget, help_text).
    # Field syntax: Field_name = forms.FieldType(attributes)
    # Example attributes: max_length, help_text, widget, required, etc.
    # PasswordInput() widget ensures that the password is hidden when entered.
    
    