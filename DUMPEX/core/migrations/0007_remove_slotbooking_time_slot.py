# Generated by Django 5.1.1 on 2024-10-29 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_slotbooking_wallet_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slotbooking',
            name='time_slot',
        ),
    ]
