from  django import forms

from .models import *

class CollegeForm(forms.ModelForm):
    class Meta:
        model = CollegeModel
        fields = '__all__'
