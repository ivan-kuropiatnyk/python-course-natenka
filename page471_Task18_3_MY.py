# -*- coding: utf-8 -*-
"""
Задание 18.3
"""
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import pprint
import yaml
import re
from page471_Task18_1_MY import send_show_command
from page471_Task18_2_MY import send_config_commands
def send_commands(device, * ,show = 'False', config = 'False'):
    try:
        if show != 'False' and config != 'False':
            raise ValueError("Можно передавать только один из аргументов show/config")
        elif show != 'False' and config == 'False':
            print(send_show_command(device, show))
        elif show == 'False' and config != 'False':
            print(send_config_commands(device, config))
    except (TypeError):
        print('send_commands() takes 1 positional argument but 2 were given')

if __name__ == "__main__":
    commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
    command = "sh ip int br"
    with open("page471_Task18_MY_devices_cut.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_commands(dev, config=commands))