from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators


class SimpleCustomers(AbstractUser):
    three_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    address = models.TextField(verbose_name='Адрес')
    avatar = models.ImageField(upload_to='profile_pictures', blank=True, null=True, verbose_name='Фото профиля')
    about = models.CharField(max_length=100, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Розничный покупатель'
        verbose_name_plural = 'Розничные покупатели'


class QRCode(models.Model):
    code = models.CharField(max_length=14, verbose_name='Штрих-код')


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    code = models.OneToOneField(QRCode, on_delete=models.CASCADE, verbose_name='Штрих-код продукта')
    special_code = models.CharField(max_length=14, db_index=True, verbose_name='Код номенклатуры')
    price = models.FloatField(verbose_name='цена', validators=[validators.MinValueValidator(limit_value=1.0,
                                                                                            message='Неверная цена')])
    package = models.BooleanField(verbose_name='Упковка продукции', default=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)
