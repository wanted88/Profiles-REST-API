from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

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
