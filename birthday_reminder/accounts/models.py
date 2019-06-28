from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            date_of_birth=date_of_birth,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, date_of_birth, password):
        user = self.create_user(
            email,
            username,
            date_of_birth,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    usernmae = models.CharField(max_length=40, unique=True)
    date_of_birth = models.DateField()
    avator = models.ImageField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["username", "date_of_birth"]

    def __str__(self):
        return self.username
