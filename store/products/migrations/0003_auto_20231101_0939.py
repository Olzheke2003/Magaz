# Generated by Django 3.2.12 on 2023-11-01 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='productcategori',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
    ]
