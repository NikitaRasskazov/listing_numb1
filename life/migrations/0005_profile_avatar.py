# Generated by Django 4.2.10 on 2024-02-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0004_merge_20240210_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatar/', verbose_name='Аватар'),
        ),
    ]
