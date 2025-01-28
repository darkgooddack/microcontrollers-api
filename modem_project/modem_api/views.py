from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class ModemListView(generics.ListAPIView):
    queryset = Modem.objects.all()
    serializer_class = ModemSerializer

class SensorListView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class CounterListView(generics.ListAPIView):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class CreateModemData(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        # Извлекаем или создаем объект Modem
        modem = Modem.objects.get(mac_address=data["mac"])  # По MAC-адресу находим модем

        # Создаем датчики для данного модема
        for i in range(1, 3):
            sensor_name = data.get(f"name{i}")
            vibrations = data.get(f"vibrations{i}")
            temperature = data.get(f"temperature{i}")

            # Создание датчиков
            sensor = Sensor.objects.create(
                modem=modem,  # Связываем с модемом
                mac_address=sensor_name,
                vibrations=vibrations,
                temperature=temperature
            )

        # Создание счетчиков для данного модема
        for counter_data in data["counters"]:
            counter_data["modem"] = modem  # Устанавливаем модем для счетчика
            # Важно: добавляем поле 'time', которое требуется для создания счетчика
            counter_data["time"] = data["time"]  # Передаем список времени
            # Создаем счетчик
            Counter.objects.create(**counter_data)

        # Возвращаем успешный ответ
        return Response({"message": "Data successfully saved"}, status=status.HTTP_201_CREATED)