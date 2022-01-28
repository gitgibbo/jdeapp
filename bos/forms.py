from django import forms
from .models import BOS

class BOSForm(forms.ModelForm):
    class Meta:
        model = BOS
        fields = ['Area','Shift', 'Topic', 'Comments']

