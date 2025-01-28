# Generated by Django 5.1.5 on 2025-01-28 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.CharField(max_length=17, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=20)),
                ('energy', models.JSONField()),
                ('cos_fi_a', models.JSONField()),
                ('cos_fi_b', models.JSONField()),
                ('cos_fi_c', models.JSONField()),
                ('cos_fi_common', models.JSONField()),
                ('freq_a', models.JSONField()),
                ('freq_b', models.JSONField()),
                ('freq_c', models.JSONField()),
                ('freq_common', models.JSONField()),
                ('voltage_a', models.JSONField()),
                ('voltage_b', models.JSONField()),
                ('voltage_c', models.JSONField()),
                ('voltage_common', models.JSONField()),
                ('current_a', models.JSONField()),
                ('current_b', models.JSONField()),
                ('current_c', models.JSONField()),
                ('current_common', models.JSONField()),
                ('whole_power_a', models.JSONField()),
                ('whole_power_b', models.JSONField()),
                ('whole_power_c', models.JSONField()),
                ('active_power_a', models.JSONField()),
                ('active_power_b', models.JSONField()),
                ('active_power_c', models.JSONField()),
                ('reactive_power_a', models.JSONField()),
                ('reactive_power_b', models.JSONField()),
                ('reactive_power_c', models.JSONField()),
                ('time', models.JSONField()),
                ('modem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counters', to='modem_api.modem')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.CharField(max_length=17)),
                ('vibrations', models.JSONField()),
                ('temperature', models.JSONField()),
                ('modem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='modem_api.modem')),
            ],
        ),
    ]
