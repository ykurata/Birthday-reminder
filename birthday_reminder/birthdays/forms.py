from django import forms
from . import models

class BirthdayFrom(forms.ModelForm):
    class Meta:
        model = models.Birthday
        fields = [
            "name",
            "date_of_birth"
        ]

    date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=('%Y-%m-%d', ),
        help_text = "yyyy-mm-dd"
        )
