from django.shortcuts import render
# from django.views import generic

from . import models
from . import forms


def create_birthday(request, pk=None):
    form = forms.BirthdayFrom()

    return render(
        request,
        'birthday/birthday_form.html', {
        'form': form })
