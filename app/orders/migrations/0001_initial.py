# Generated by Django 3.1.4 on 2021-01-13 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_adress_district_province'),
        ('cart', '0003_auto_20210105_2248'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('status', models.CharField(choices=[('creado', 'Creado'), ('pagado', 'Pagado'), ('enviado', 'Enviado'), ('reembolsado', 'Reembolsado')], default='created', max_length=120)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adress', to='accounts.adress')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('modified_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Modificado por')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]