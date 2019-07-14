from django.conf import settings
from django.db import models
from djangoyearlessdate.models import YearlessDateField


class Birthday(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, help_text="yyyy-mm-dd")
    
    def __str__(self):
        return self.name
