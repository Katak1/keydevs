# Generated by Django 4.2 on 2024-08-28 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_code_expiration_user_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_chat_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
