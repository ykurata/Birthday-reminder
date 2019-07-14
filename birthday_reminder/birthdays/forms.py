from django import forms
from . import models

class BirthdayFrom(forms.ModelForm):
    class Meta:
        model = models.Birthday
        fields = [
            "name",
            "date_of_birth"
        ]
    
