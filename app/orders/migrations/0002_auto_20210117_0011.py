# Generated by Django 3.1.4 on 2021-01-17 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial_manual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]