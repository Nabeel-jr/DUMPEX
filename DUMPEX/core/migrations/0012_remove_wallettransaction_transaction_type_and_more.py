# Generated by Django 5.1.2 on 2024-10-30 23:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_wallettransaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallettransaction',
            name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='wallettransaction',
            name='user',
        ),
        migrations.AddField(
            model_name='wallettransaction',
            name='admin',
            field=models.ForeignKey(default=7, limit_choices_to={'user_type': 4}, on_delete=django.db.models.deletion.CASCADE, related_name='wallet_transactions_as_admin', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wallettransaction',
            name='manager',
            field=models.ForeignKey(default=5, limit_choices_to={'user_type': 3}, on_delete=django.db.models.deletion.CASCADE, related_name='wallet_transactions_as_manager', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
