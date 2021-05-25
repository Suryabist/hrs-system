import uuid

from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

# Create your models here.
from hospital.user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.UUIDField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
        default=uuid.uuid4
    )
    email = models.EmailField(max_length=45, unique=True, error_messages={
        'unique': "A user with that email already exists.",
    }, )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    hospital = models.CharField(max_length=256)
    is_admin = models.BooleanField(default=False)
    is_hospital = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=10, null=True, blank=True, unique=True)
    last_activity = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    REGISTRATION_FIELDS = ['email', 'first_name', 'last_name', 'password', 'hospital', 'phone_number',
                           ]

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super().save(*args, **kwargs)
