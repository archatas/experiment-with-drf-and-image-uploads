import os
import sys

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as UserManagerBase
from django.utils import timezone

if "makemigrations" in sys.argv:
    from django.utils.translation import gettext_noop as _
else:
    from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class UserManager(UserManagerBase):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        if not username:
            username = email
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if not username:
            username = email
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    # change username to non-editable non-required field
    username = models.CharField(
        _("username"), max_length=150, editable=False, blank=True
    )
    # change email to unique and required field
    email = models.EmailField(_("email address"), unique=True)

    avatar = models.ImageField(_("Avatar"), upload_to=upload_to, blank=True)

    bio = models.TextField(_("Bio"), blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
