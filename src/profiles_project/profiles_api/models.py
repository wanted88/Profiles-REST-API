from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user models"""

    def create_user(self, email, name, password=None):
    """Create a new user profiles object."""

    if not email:
        raise ValueError('User must have an email address')

    email = self.normalize_email(email)
    user = self.model(email=email, name=name)

    user.set_password(password)
    user.save(using=self.db)

    return user

def create_superuser(self, email, name, password):
    """Creates and saves a new superuser with given details"""

    user = self.create_user(email, name, password)

    user.is_superuser = True
    user.is_staff = True

    user.save(using=self.db)

class UserProfiles(AbstracBaseUser, PermissionsMixin):
        """Respents a "user profiles" inside our system"""

        email = models.EmailField(max_lenght=255, unique=True)
        name = models.CharField(max_lenght=255)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)

        objects = UserProfileManager()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELD = ['name']

        def get_full_name(self):
            """Used to get a user full name"""

            return self.name

        def get_short_name(self):
            """Used to get a user short name"""

            return self.name

        def __str__(self):
            """Django uses this when it need to convert the object to string"""

            return self.email
