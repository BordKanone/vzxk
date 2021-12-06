# Generated by Django 3.2.9 on 2021-12-06 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vzxk', '0015_auto_20211201_0046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vzxk.product'),
        ),
        migrations.DeleteModel(
            name='ProductsOrder',
        ),
    ]
