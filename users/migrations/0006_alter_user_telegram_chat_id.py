# Generated by Django 4.2 on 2024-08-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_telegram_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_chat_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
