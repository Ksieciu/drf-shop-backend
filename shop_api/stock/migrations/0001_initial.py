# Generated by Django 3.1.5 on 2021-01-26 10:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('promotion_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('promotion_going', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('stock', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('availability', models.CharField(blank=True, choices=[('IN', 'In Stock'), ('OUT', 'Out of stock'), ('SOON', 'Available soon')], default='OUT', max_length=4)),
                ('category', models.ManyToManyField(to='stock.Category')),
            ],
        ),
    ]
