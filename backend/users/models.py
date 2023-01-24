import jwt, time
from datetime import timedelta, datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class BaseUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'

    objects = BaseUserManager()

    @property
    def token(self):
        dt = datetime.now() + timedelta(days=1)
        token = jwt.encode({
            'id': self.id,
            'exp': int(time.mktime(dt.timetuple()))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')


class Employee(BaseUser):
    code = models.IntegerField()


class Client(BaseUser):
    full_address = models.TextField()
