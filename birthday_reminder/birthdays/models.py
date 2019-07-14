from django.conf import settings
from django.db import models
import datetime


class Birthday(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, help_text="yyyy-mm-dd")

    @property
    def age(self):
        return int((datetime.datetime.now().date() - self.date_of_birth).days / 365.25 )

    def __str__(self):
        return self.name
