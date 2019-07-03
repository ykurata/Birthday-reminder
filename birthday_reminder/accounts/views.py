from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect

from . import forms
from . import models


def signup(request):
    if request == "POST":
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleand_data.get('username')
            raw_password = form.cleaed_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect("home")
    else:
        form = forms.UserCreateForm()
    return render(request, 'accounts/sign_up.html', {'form': form})
