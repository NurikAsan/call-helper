from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager


class User(AbstractUser):
    phone_number = PhoneNumberField(unique=True, null=True)

    objects = CustomUserManager()
