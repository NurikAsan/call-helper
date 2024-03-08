from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='profile',verbose_name="Пользователь")
    telegram_id = models.CharField(max_length=20, verbose_name="Id Telegram", null=True, blank=True)

    class Meta:
        verbose_name = "Профиль Пользователя"
        verbose_name_plural = "Профиль Пользователей"

    def __str__(self):
        return f'{self.user}'