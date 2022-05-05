from django.urls import path

from .views import WeekView

urlpatterns = [
    path('', WeekView.as_view()), # по адресу 'host/' будет выводится вьюха WeekView
]