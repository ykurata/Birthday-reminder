from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect

from . import forms
from . import models


def signup(request):
    if request.method == "POST":
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
        return redirect("home")
    else:
        form = forms.UserCreateForm()
    return render(request, 'accounts/sign_up.html', {'form': form})


def page_not_found(request):
    response = render(request, '404.html')
    response.status_code = 404
    return response
