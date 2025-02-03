from rest_framework import serializers
from .models import Modem, Sensor, Counter

#Всё супер но id желательно возвращать

class SensorSerializer(serializers.ModelSerializer):
    modem_mac_address = serializers.CharField(source='modem.mac_address', read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'mac_address', 'vibrations', 'temperature', 'modem_mac_address']


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'


class ModemSerializer(serializers.ModelSerializer):
    sensors = SensorSerializer(many=True)
    counters = CounterSerializer(many=True)

    class Meta:
        model = Modem
        fields = ['id', 'mac_address', 'sensors', 'counters']


class PostDataSerializer(serializers.Serializer):
    mac = serializers.CharField(max_length=17)
    name1 = serializers.CharField(max_length=17)
    vibrations1 = serializers.ListField(child=serializers.IntegerField())
    temperature1 = serializers.ListField(child=serializers.IntegerField())
    name2 = serializers.CharField(max_length=17)
    vibrations2 = serializers.ListField(child=serializers.IntegerField())
    temperature2 = serializers.ListField(child=serializers.IntegerField())
    counters = CounterSerializer(many=True)
    time = serializers.ListField(child=serializers.CharField())
