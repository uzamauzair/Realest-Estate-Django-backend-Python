from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name,password=None):
        if not email:
            raise ValueError('Users must have an email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # save the password in the db with hashing
        user.save() # user.save(using=self._db), since we don't have more than 1 db we won't use this

        return user
    
    def create_superuser(self, email, name,password):
        user = self.create_user(email, name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
        
    ''''Database Model'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    # django usually use username for the auth, but here we use
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email