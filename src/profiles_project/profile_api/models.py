from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    #Help django work with our custom user model

    def create_user(self, email, name, password):
        # Creates a new user object
        if not email:
            raise ValueError('User must have a email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        # Creates a new super user

        user = self.create_user(email, name, password)
        self.is_superuser = True
        self.is_staff = True

        user.save(using=self._db)

        return user
        


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''' Represents a "user profile"'''

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    #helper functions
    def get_full_name(self):
        # Gives user's full name

        return self.name

    def get_short_name(self):
        # Gives user's short name

        return self.name

    def __str__(self):
        return self.email