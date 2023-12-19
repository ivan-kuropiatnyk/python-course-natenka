# -*- coding: utf-8 -*-
"""
Задание 18.2a
"""
from netmiko import ConnectHandler
import yaml

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]


def send_config_commands(device, config_commands, log=False):
    if log:
        print(f"Подключаюсь к {device['host']}...")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result

if __name__ == "__main__":
    with open("page471_Task18_OTVET_devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_config_commands(dev, commands, log=True))