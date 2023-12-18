import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manger import UserManager
# Create your models here.
class Roles(models.Model):
    role_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(max_length=225, primary_key=True, blank=True, unique=True)
    # user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=100)
    # birthday = models.DateField(blank=True, null=True, default=datetime.date.today())
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to="images/")

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'address', 'gender']

    objects = UserManager()

class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'{self.user.last_name}-passcode'


