# Generated by Django 3.1.5 on 2021-01-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
