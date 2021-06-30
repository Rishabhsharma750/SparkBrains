from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database models for users in the system"""
    email=models.EmailField(max_length=500,unique=True)
    name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retreive full name of user"""
        return self.name

    def short_name(self):
        """Retreive short name of user"""
        return self.name

    def __str__(self):
        """Retreive string representation of our user"""
        return self.email

class Student(models.Model):
    user_profile=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.name
