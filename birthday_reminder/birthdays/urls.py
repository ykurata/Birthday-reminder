from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^(?P<pk>\d+)/edit/$", views.edit_birthday, name="edit"),
    url(r"^all/$", views.birthday_list, name="list"),
    url(r"^create/$", views.create_birthday, name="create"),
    url(r"^(?P<pk>\d+)/delete/$", views.delete_birthday, name="delete"),
]
