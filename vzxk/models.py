import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
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
    qr_code = models.CharField(max_length=14, verbose_name='Штрих-код')

    def __str__(self):
        return f'{self.qr_code}'


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    code = models.OneToOneField(QRCode, on_delete=models.CASCADE, verbose_name='Штрих-код продукта')
    price = models.DecimalField(verbose_name='цена', max_digits=3, decimal_places=2,
                                validators=[validators.MinValueValidator(limit_value=1.00, message='Неверная цена')])

    package = models.BooleanField(verbose_name='Упковка продукции', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)


class Contragent(AbstractUser):
    company = models.CharField(max_length=255, blank=False, null=False, verbose_name='Наименование организации')
    three_name = models.CharField(max_length=255, verbose_name='Отчество')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    ogrn = models.CharField(max_length=13, verbose_name='ОГРН')
    address = models.TextField(verbose_name='Адрес')
    contract = models.OneToOneField('Contracts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
        ordering = ('company',)


class Contracts(models.Model):
    name = models.OneToOneField(Contragent, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Контрагент')
    document = models.FileField(upload_to='contracts/%Y/%m/%d/', verbose_name='Файл договора')

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'
        ordering = ('name',)


class Order(models.Model):
    customer = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='customer', fk_field='object_id')

    products = models.ManyToManyField('ProductForOrder')
    address_to = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес доставки')
    number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество продуктов')
    total_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Общая цена '
                                                                                                          'заказа')
    date_order = models.DateTimeField(auto_now=True, verbose_name='Дата поступления')
    date_complete = models.DateTimeField(blank=True, null=True, verbose_name='Дата поступления в пункт выдачи')

    def save(self, *args, **kwargs):
        self.date_complete = datetime.datetime.now() + datetime.timedelta(days=3)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Заказ: {self.pk}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('date_order', 'date_complete')


class ProductForOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    numbers = models.PositiveIntegerField()
