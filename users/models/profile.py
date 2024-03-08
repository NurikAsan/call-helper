from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('users.User', models.CASCADE, related_name='profile',verbose_name="Пользователь")
    telegram_id = models.CharField(max_length=20, verbose_name="Id Telegram", null=True, blank=True)

    class Meta:
        verbose_name = "Профиль Пользователя"
        verbose_name_plural = "Профиль Пользователей"

    def __str__(self):
        return f'{self.user}'