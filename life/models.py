from django.db import models
from django.contrib.auth import get_user_model


DjangoUser = get_user_model()


GENRE_BOARD_GAMES = [
    ('strategy', 'Стратегическая'),
    ('economic', 'Экономическая'),
    ('combat', 'Боевая'),
    ('cooperative', 'Кооперативная'),
    ('mobile', 'Подвижная'),
    ('card', 'Карточная'),
    ('duos', 'Один на один')
]


class User(DjangoUser):

    class Meta:
        proxy = True

    def get_profile(self):
        return Profile.objects.get_or_create(user_id=self.pk)[0]


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='профиль',
        on_delete=models.CASCADE,
        related_name='profile'
    )
    first_name = models.CharField(
        'Имя',
        max_length=255
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=255
    )
    patronymic = models.CharField(
        'Отчество',
        max_length=255
    )
    friends = models.ManyToManyField(
        'self',
        verbose_name='Друзья',
        related_name='profiles',
        blank=True
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'


class BoardGame(models.Model):
    name = models.CharField(
        'Название',
        max_length=255
    )
    count_players = models.SmallIntegerField(
        'Количество игроков'
    )
    genre = models.ManyToManyField(
        'GenreBoardGame',
        verbose_name='Жанр',
        related_name='genres'
    )
    player = models.ForeignKey(
        Profile,
        verbose_name='Владелец',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='board_games'
    )

    class Meta:
        verbose_name = 'Настольная игра'
        verbose_name_plural = 'Настольные игры'

    def __str__(self):
        return self.name


class GenreBoardGame(models.Model):
    name = models.CharField(
        'тип',
        max_length=255,
        choices=GENRE_BOARD_GAMES,
    )
    description = models.CharField(
        'Краткое описание жанра',
        max_length=255
    )

    class Meta:
        verbose_name = 'Жанры настольной игры'
        verbose_name_plural = 'Жанры настольных игр'

    def __str__(self):
        return self.name
