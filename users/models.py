from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# definissons les permissions pour notre application
class Permission(models.Model):
    name = models.CharField(max_length=200)

# Le role de  nos utilisateurs


class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
