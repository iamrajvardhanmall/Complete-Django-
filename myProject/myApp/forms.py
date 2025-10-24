from django import forms

class feedbackForm(forms.Form):
    title = forms.CharField(label = 'Title', max_length = 50, widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title Here'}))
    # class and placeholder are added as attributes to the widget
    
    subject = forms.CharField(label = 'Subject Description', max_length = 200, widget = forms.Textarea)


