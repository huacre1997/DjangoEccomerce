# Generated by Django 3.1.1 on 2020-10-26 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201025_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(error_messages={'unique': 'Ya ingresó esa subcategoria'}, max_length=100, unique=True),
        ),
    ]
