from django.db import models
from django.contrib.auth import get_user_model
from ..constants import BREAK_STATUS_CREATED
from .dicts import BreakStatus

User = get_user_model()

class Break(models.Model):
    replacement = models.ForeignKey(
        'breaks.Replacement', models.CASCADE, 'breaks', verbose_name='Смена',
    )
    employee = models.ForeignKey(
        User, models.CASCADE, 'breaks', verbose_name='Сотрудник',
    )
    break_start = models.TimeField('Начало обеда', null=True, blank=True,)
    break_end = models.TimeField('Конец обеда', null=True, blank=True,)
    duration = models.PositiveSmallIntegerField('Длительность обеда', null=True, blank=True)
    status = models.ForeignKey(
        'breaks.BreakStatus', models.RESTRICT, 'breaks', verbose_name='Статус',
        blank=True,
    )

    class Meta:
        verbose_name = 'Обеденный перерыв'
        verbose_name_plural = 'Обеденный перерывы'
        ordering = ('-replacement__date', 'break_start')

    def __str__(self):
        return f'Обед пользователя {self.employee} ({self.pk})'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            status, created = BreakStatus.objects.get_or_create(
                code=BREAK_STATUS_CREATED, defaults={
                    'name': 'Test',
                    'is_active': True,
                    'sort': 777
                }
            )
            self.status = status
        return super(Break, self).save(*args, **kwargs)
