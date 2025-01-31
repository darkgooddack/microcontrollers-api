from django.urls import path

# импортировать рекомендуется явно
from .views import ModemListView, SensorListView, CounterListView, CreateModemData

urlpatterns = [
    path('modems/all', ModemListView.as_view()),
    path('sensors/all', SensorListView.as_view()),
    path('counters/all', CounterListView.as_view()),
    path('create_modem_data', CreateModemData.as_view()),
]