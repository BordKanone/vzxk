# Generated by Django 3.2.9 on 2021-11-19 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vzxk', '0003_alter_simplecustomers_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplecustomers',
            name='about',
            field=models.CharField(blank=True, max_length=100, verbose_name='Описание'),
        ),
    ]
