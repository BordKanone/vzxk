from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser


class SimpleCustomers(AbstractUser):
    three_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    address = models.TextField(verbose_name='Адрес')
    avatar = models.ImageField(upload_to='profile_pictures', blank=True, null=True, verbose_name='Фото профиля')
    about = models.CharField(max_length=100,blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Розничный покупатель'
        verbose_name_plural = 'Розничные покупатели'


