from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from datetime import datetime

from . import models
from . import forms


@login_required
def birthday_list(request):
    """show birthdays list"""
    birthdays = models.Birthday.objects.all().order_by('month').order_by('day')
    return render(request, 'birthday/birthday_list.html', {'birthdays': birthdays})


@login_required
def create_birthday(request, pk=None):
    """create a new birthday"""
    form = forms.BirthdayFrom()

    if request.method == "POST":
        form = forms.BirthdayFrom(request.POST)

        if form.is_valid():
            birthday = form.save(commit=False)
            birthday.user = request.user
            birthday.save()
        return HttpResponseRedirect(reverse("home"))

    return render(
        request,
        'birthday/birthday_form.html', {
        'form': form })


@login_required
def edit_birthday(request, pk):
    """update a birthday"""
    try:
        birthday = models.Birthday.objects.get(pk=pk, user=request.user)
    except ObjectDoesNotExist:
        birthday = None

    form = forms.BirthdayFrom(instance=birthday)

    if request == "POST":
        form = forms.BirthdayFrom(request.POST)

        if form.is_valid():
            birthday = form.save(commit=False)
            birthday.user = request.user
            birthday.save()
        return HttpResponseRedirect(reverse("home"))
    return  render(
        request,
        'birthday/birthday_form.html', {
        'form': form })


@login_required
def delete_birthday(request, pk):
    """delete a birthday"""
    try:
        birthday = models.Birthday.objects.get(pk=pk, user=request.user)
    except ObjectDoesNotExist:
        birthday = None
    birthday.delete()
    return redirect('home')
