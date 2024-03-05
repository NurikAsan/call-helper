from django.contrib.auth import get_user_model
from django.db import models
from common.models.mixins import BaseDictModel


class ReplacementStatus(BaseDictModel):
    class Meta:
        verbose_name = 'Статус смены'
        verbose_name_plural = 'Статусы смены'
    

class BreakStatus(BaseDictModel):
    class Meta:
        verbose_name = 'Статус обеда'
        verbose_name_plural = 'Статусы обеда'