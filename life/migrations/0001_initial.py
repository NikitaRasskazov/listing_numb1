# Generated by Django 3.2 on 2024-02-07 17:18

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreBoardGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('strategy', 'Стратегическая'), ('economic', 'Экономическая'), ('combat', 'Боевая'), ('cooperative', 'Кооперативная'), ('mobile', 'Подвижная'), ('card', 'Карточная'), ('duos', 'Один на один')], max_length=255, verbose_name='тип')),
                ('description', models.CharField(max_length=255, verbose_name='Краткое описание жанра')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('friends', models.ManyToManyField(related_name='_life_profile_friends_+', to='life.Profile', verbose_name='Друзья')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='life.user', verbose_name='профиль')),
            ],
        ),
        migrations.CreateModel(
            name='BoardGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('players', models.SmallIntegerField(verbose_name='Количество игроков')),
                ('genre', models.ManyToManyField(related_name='genres', to='life.GenreBoardGame', verbose_name='Жанр')),
            ],
        ),
    ]