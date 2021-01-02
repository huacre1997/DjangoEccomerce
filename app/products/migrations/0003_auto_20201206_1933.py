# Generated by Django 3.1.3 on 2020-12-07 00:33

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201206_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='before',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, verbose_name='Precio anterior'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children2', to='products.category', verbose_name='Categoría'),
        ),
    ]