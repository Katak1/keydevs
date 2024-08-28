# Generated by Django 4.2 on 2024-08-27 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='posts.post'),
        ),
    ]
