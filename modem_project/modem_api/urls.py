from django.urls import path
from .views import *

urlpatterns = [
    path('modems/all', ModemListView.as_view()),
    path('sensors/all', SensorListView.as_view()),
    path('counters/all', CounterListView.as_view()),
    path('create_modem_data', CreateModemData.as_view()),
]