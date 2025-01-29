from django.db import models

class Modem(models.Model):
    mac_address = models.CharField(max_length=17, unique=True)

    def str(self):
        return f"Modem: {self.mac_address}"


class Sensor(models.Model):
    modem = models.ForeignKey(Modem, related_name='sensors', on_delete=models.CASCADE)
    mac_address = models.CharField(max_length=17)
    vibrations = models.JSONField()
    temperature = models.JSONField()

    def str(self):
        return f"Sensor: {self.mac_address} (Modem: {self.modem.mac_address})"


class Counter(models.Model):
    modem = models.ForeignKey(Modem, related_name='counters', on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    energy = models.JSONField()
    cos_fi_a = models.JSONField()
    cos_fi_b = models.JSONField()
    cos_fi_c = models.JSONField()
    cos_fi_common = models.JSONField()
    freq_a = models.JSONField()
    freq_b = models.JSONField()
    freq_c = models.JSONField()
    freq_common = models.JSONField()
    voltage_a = models.JSONField()
    voltage_b = models.JSONField()
    voltage_c = models.JSONField()
    voltage_common = models.JSONField()
    current_a = models.JSONField()
    current_b = models.JSONField()
    current_c = models.JSONField()
    current_common = models.JSONField()
    whole_power_a = models.JSONField()
    whole_power_b = models.JSONField()
    whole_power_c = models.JSONField()
    active_power_a = models.JSONField()
    active_power_b = models.JSONField()
    active_power_c = models.JSONField()
    reactive_power_a = models.JSONField()
    reactive_power_b = models.JSONField()
    reactive_power_c = models.JSONField()
    time = models.JSONField()

    def str(self):
        return f"Counter: {self.address} (Modem: {self.modem.mac_address})"
