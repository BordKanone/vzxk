import datetime

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import AbstractUser, User
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
    price = models.DecimalField(verbose_name='цена', max_digits=3, decimal_places=2,
                                validators=[validators.MinValueValidator(limit_value=1.00, message='Неверная цена')])

    package = models.BooleanField(verbose_name='Упковка продукции', default=False)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Contragent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=False, null=False, verbose_name='Наименование')
    real_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Физическое ФИО')
    ur_address = models.CharField(max_length=255, verbose_name='Юридический адрес')
    real_address = models.CharField(max_length=255, blank=False, null=False, verbose_name='Физический адрес')
    code = models.CharField(max_length=5,blank=False, null=False, verbose_name='Код номенклатуры')
    contract_number = models.ForeignKey('Contracts', on_delete=models.CASCADE,
                                        db_index=True, blank=False, null=False, verbose_name='Номер договора')

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
        ordering = ('name',)


class Contracts(models.Model):
    name = models.OneToOneField(Contragent, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Контрагент')
    code = models.CharField(max_length=22, verbose_name='Номер договора')
    document = models.FileField(upload_to='contracts/%Y/%m/%d/', verbose_name='Файл договора')

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'
        ordering = ('name',)


class Order(models.Model):
    code = models.CharField(max_length=10,
                            db_index=True, unique=True, blank=False, null=False,
                            verbose_name='Номер заказа')
    contragent = models.ForeignKey(Contragent, on_delete=models.CASCADE,
                                   blank=False, null=False, verbose_name='Заказчик')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    address_to = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес доставки')
    content_type_object = GenericForeignKey('content_type', 'object_id')
    number = models.PositiveIntegerField(verbose_name='Количество продуктов')
    total_price = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, verbose_name='Общая цена заказа')
    date_order = models.DateTimeField(auto_now=True, verbose_name='Дата поступления')
    date_complete = models.DateTimeField(verbose_name='Дата поступления в пункт выдачи')

    def save(self, *args, **kwargs):
        self.total_price = self.number * self.content_type_object.price
        self.address_to = self.contragent.real_address
        self.date_complete = datetime.datetime.now() + datetime.timedelta(days=2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.code} - {self.content_type_object.name} to {self.contragent.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('date_order', 'date_complete')

