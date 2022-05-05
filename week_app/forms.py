from django.forms import ModelForm
from .models import WeekSearch


class WeekForm(ModelForm):
    '''Форма Django с нужными полями для отправки запроса'''
    class Meta:
        model = WeekSearch
        fields = ['day', 'month', 'year']
