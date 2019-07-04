from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^all/$", views.birthday_list, name="list"),
    url(r"^create/$", views.create_birthday, name="create"),
]
