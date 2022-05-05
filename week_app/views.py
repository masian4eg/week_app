from django.shortcuts import render
from django.views.generic import FormView

from .forms import WeekForm
from .logic import which_week


class WeekView(FormView):
    """Представление в котором будет отображаться форма WeekForm, на шаблоне week.html
    При удачном заполнении формы перебрасывает в шаблон "week_result" с со значением answer"""
    form_class = WeekForm
    template_name = 'week.html'
    success_url = '/answer/'

    def post(self, request, *args, **kwargs):
        """Переопределяем метод post - если форма заполнена верно применяем метод из logic.py для подсчета недели"""
        form = self.get_form()
        
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'week_result.html', {'answer': which_week(data['day'], data['month'], data['year'])})
