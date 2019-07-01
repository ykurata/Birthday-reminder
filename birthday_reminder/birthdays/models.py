from django.conf import settings
from django.db import models


class Birthday(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.date_of_birth
