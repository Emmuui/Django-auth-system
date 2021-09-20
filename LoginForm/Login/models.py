from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if email is None:
            raise ValueError("Enter a valid email address")
        if username is None:
            raise ValueError("Enter a valid username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=70, unique=True)
    username = models.CharField(max_length=40, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    date_login = models.DateTimeField(verbose_name='date_login', auto_now=True)
    is_active = models.BooleanField(verbose_name='is_active', default=True)
    is_admin = models.BooleanField(verbose_name='is_admin', default=False)
    is_staff = models.BooleanField(verbose_name='is_staff', default=False)
    is_superuser = models.BooleanField(verbose_name='is_superuser', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

