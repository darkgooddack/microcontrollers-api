from django.db import models

class Modem(models.Model):
    mac_address = models.CharField(max_length=17, unique=True)

    def str(self):
        return f"Modem: {self.mac_address}"

# Задал типы данных явно
class Sensor(models.Model):
    modem = models.ForeignKey(Modem, related_name='sensors', on_delete=models.CASCADE)
    mac_address = models.CharField(max_length=17)
    vibrations = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)
    time = models.DateTimeField() #добавил временную ветку и для сенсоров, видимо забыла

    def str(self):
        return f"Sensor: {self.mac_address} (Modem: {self.modem.mac_address})"


class Counter(models.Model):
    modem = models.ForeignKey(Modem, related_name='counters', on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    energy = models.FloatField(default=0.0)
    cos_fi_a = models.FloatField(default=0.0)
    cos_fi_b = models.FloatField(default=0.0)
    cos_fi_c = models.FloatField(default=0.0)
    cos_fi_common = models.FloatField(default=0.0)
    freq_a = models.FloatField(default=0.0)
    freq_b = models.FloatField(default=0.0)
    freq_c = models.FloatField(default=0.0)
    freq_common = models.FloatField(default=0.0)
    voltage_a = models.FloatField(default=0.0)
    voltage_b = models.FloatField(default=0.0)
    voltage_c = models.FloatField(default=0.0)
    voltage_common = models.FloatField(default=0.0)
    current_a = models.FloatField(default=0.0)
    current_b = models.FloatField(default=0.0)
    current_c = models.FloatField(default=0.0)
    current_common = models.FloatField(default=0.0)
    whole_power_a = models.IntegerField(default=0)
    whole_power_b = models.IntegerField(default=0)
    whole_power_c = models.IntegerField(default=0)
    active_power_a = models.IntegerField(default=0)
    active_power_b = models.IntegerField(default=0)
    active_power_c = models.IntegerField(default=0)
    reactive_power_a = models.IntegerField(default=0)
    reactive_power_b = models.IntegerField(default=0)
    reactive_power_c = models.IntegerField(default=0)
    time = models.DateTimeField()

    def str(self):
        return f"Counter: {self.address} (Modem: {self.modem.mac_address})"
