from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^create/$", views.create_birthday, name="create"),
]
