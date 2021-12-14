import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from rest_framework.exceptions import ValidationError


class Customer(AbstractUser):
    CUSTOMERS_TYPE_CHOICES = (
        (None, 'Тип учетной записи'),
        ('contragent', 'Контрагент'),
        ('simple_customer', 'Розничный покупатель'),
        ('employee', 'Сотрудник')
    )
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    three_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    address = models.CharField(max_length=250, verbose_name='Адрес')
    customers_type = models.CharField(max_length=25, choices=CUSTOMERS_TYPE_CHOICES, verbose_name='тип учетной записи')
    avatar = models.ImageField(upload_to='profile_pictures', blank=True, null=True, verbose_name='Фото профиля')
    about = models.CharField(max_length=100, blank=True, verbose_name='Описание')
    company = models.CharField(max_length=255, blank=True, null=False, verbose_name='Наименование организации')
    inn = models.CharField(max_length=12, blank=True, null=True, verbose_name='ИНН')
    ogrn = models.CharField(max_length=13, blank=True, null=True, verbose_name='ОГРН')
    contract = models.OneToOneField('Contracts', blank=True, null=True, on_delete=models.CASCADE)

    def get_username(self):
        return f'{self.first_name} {self.last_name}'

    def clean(self):
        if self.customers_type == 'contragent' or self.customers_type is None:
            for key in (self.company, self.inn, self.ogrn, self.contract):
                if not key:
                    raise ValidationError('Не все поля заполнены для этого типа учетной записи')
        else:
            for key in (self.company, self.inn, self.ogrn, self.contract):
                if key:
                    raise ValidationError(f'Поле {key} не должно быть заполнено для текущей учетной записи')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class QRCode(models.Model):
    qr_code = models.CharField(max_length=14, verbose_name='Штрих-код')

    class Meta:
        verbose_name = 'Штрих-код'
        verbose_name_plural = 'Штрих-коды'

    def __str__(self):
        return f'{self.qr_code}'


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    code = models.OneToOneField(QRCode, on_delete=models.CASCADE, verbose_name='Штрих-код продукта')
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=5,
                                validators=[validators.MinValueValidator(limit_value=0.10, message='Неверная цена')])

    package = models.BooleanField(verbose_name='Упковка продукции', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class ProductForOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Contracts(models.Model):
    contract_number = models.CharField(max_length=20, blank=True, verbose_name='Номер контракта')
    document = models.FileField(upload_to='contracts/%Y/%m/%d/', verbose_name='Файл договора')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'


class Order(models.Model):
    STATUS_CHOICES = (
        ('active', 'Активный'),
        ('process', 'В обработке'),
        ('completed', 'Завершенный'),
        ('aborted', 'Отмененный'),
        ('returned', 'Возврат'),
    )

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, unique=False, on_delete=models.DO_NOTHING,
                                 null=True, blank=True, verbose_name='Заказчик')
    products = models.ManyToManyField(Product, through=ProductForOrder)
    address_to = models.CharField(max_length=100, blank=True, null=True, verbose_name='Адрес доставки')
    total_quantity = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество продуктов')
    total_price = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True, verbose_name='Общая цена '
                                                                                  'заказа')
    date_order = models.DateTimeField(auto_now=True, verbose_name='Дата поступления')
    date_complete = models.DateTimeField(blank=True, null=True, verbose_name='Дата поступления в пункт выдачи')
    order_status = models.CharField(max_length=25, null=False, blank=False, choices=STATUS_CHOICES,
                                    default=STATUS_CHOICES[1][1])

    def save(self, *args, **kwargs):
        self.address_to = self.customer.address
        self.date_complete = datetime.datetime.now() + datetime.timedelta(days=3)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Заказ: {self.pk}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('date_order', 'date_complete')
