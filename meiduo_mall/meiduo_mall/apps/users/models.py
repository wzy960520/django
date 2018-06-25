from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class user(AbstractUser):
    moblie = models.CharField(max_length=13,unique=False,verbose_name='手机号')
    class meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name