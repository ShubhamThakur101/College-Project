from django import forms
from .models import Table_details

class AddDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Table_details 
        fields = ("day","time","subject","tname","sclass","dname")
        widgets = {
            'day':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Day'}),
            'time':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Time(ex-11:00-12:00)'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Subject Name'}),
            'tname':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Teacher Name'}),
            'sclass':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Class Name'}),
            'dname':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Department Name'})
        }

