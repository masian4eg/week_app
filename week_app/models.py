from django.db import models


class WeekSearch(models.Model):
    """Определяем модель Django которая будет принимать данные (день, месяц, год) для запроса номера недели"""
    day = models.PositiveIntegerField(help_text='Введите число месяца')
    month = models.PositiveIntegerField(help_text='Введите номер месяца')
    year = models.PositiveIntegerField(help_text='Введите год из диапазона 2019-2022')
