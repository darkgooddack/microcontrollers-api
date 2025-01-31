import datetime as dt

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

# импортировать рекомендуется явно
from .models import Modem, Sensor, Counter
from .serializers import ModemSerializer, SensorSerializer, CounterSerializer


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
    def post(self, request):
        data = request.data

        modem, created = Modem.objects.get_or_create(mac_address=data["mac"])


        for i in range(1, 3):
            sensor_name = data.get(f"name{i}")
            vibrations = data.get(f"vibrations{i}")
            temperature = data.get(f"temperature{i}")

            vibrations = vibrations[-1] if vibrations else None
            temperature = temperature[-1] if temperature else None
            time_mark = data.get("time", [dt.datetime.now()])[-1]

            #убрал неиспользуемыу переменные
            Sensor.objects.update_or_create(
                modem=modem,
                mac_address=sensor_name,
                defaults={"vibrations": vibrations, "temperature": temperature, "time": time_mark}
            )

        for counter_data in data["counters"]:
            counter_data["modem"] = modem
            counter_data["time"] = data["time"][-1]

            for field in ["energy", "cos_fi_a", "cos_fi_b", "cos_fi_c", "cos_fi_common",
                          "freq_a", "freq_b", "freq_c", "freq_common", "voltage_a", "voltage_b",
                          "voltage_c", "voltage_common", "current_a", "current_b", "current_c",
                          "current_common", "whole_power_a", "whole_power_b", "whole_power_c",
                          "active_power_a", "active_power_b", "active_power_c",
                          "reactive_power_a", "reactive_power_b", "reactive_power_c"]:
                if counter_data.get(field):
                    counter_data[field] = counter_data[field][-1]

            # убрал неиспользуемыу переменные
            Counter.objects.update_or_create(
                modem=modem,
                time=counter_data["time"],
                defaults={k: v for k, v in counter_data.items() if k != "modem" and k != "time"}
            )

        return Response({"message": "Data successfully saved"}, status=status.HTTP_201_CREATED)
