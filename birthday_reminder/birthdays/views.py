from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect

from datetime import date

from . import models
from . import forms


@login_required
def birthday_list(request):
    """show birthdays list"""
    today = date.today()
    birthdays = models.Birthday.objects.all().order_by('date_of_birth')
    bday = birthdays.filter(date_of_birth__month=today.month, date_of_birth__day=today.day)

    return render(request, 'birthday/birthday_list.html', {'birthdays': birthdays, 'bday': bday })


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
        return HttpResponseRedirect(reverse("birthdays:list"))

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

    if request.method == "POST":
        form = forms.BirthdayFrom(request.POST, instance=birthday)

        if form.is_valid():
            birthday = form.save(commit=False)
            birthday.user = request.user
            birthday.save()
        return HttpResponseRedirect(reverse("birthdays:list"))
    return  render(
        request,
        'birthday/birthday_form.html', {
        'form': form })


@login_required
def confirm_delete(request, pk):
    """Confirm deletion of a birthday"""
    try:
        birthday = models.Birthday.objects.get(pk=pk, user=request.user)
    except ObjectDoesNotExist:
        birthday = None
    return render(request, 'birthday/confirm.html', {'birthday': birthday})


@login_required
def delete_birthday(request, pk):
    """delete a birthday"""
    try:
        birthday = models.Birthday.objects.get(pk=pk, user=request.user)
    except ObjectDoesNotExist:
        birthday = None
    birthday.delete()
    return redirect('home')
