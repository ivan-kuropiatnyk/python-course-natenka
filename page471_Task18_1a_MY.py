# -*- coding: utf-8 -*-
"""
Задание 18.1a
"""
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml
import pprint
def send_show_command(device, command):
    #result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
            #result[command] = output
        return output
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
if __name__ == "__main__":
    command = "sh ip int br"
    with open("page471_Task18_MY_devices_cut_error.yaml") as f:
        devices = yaml.safe_load(f)
        for dev in devices:
            print(send_show_command(dev, command))