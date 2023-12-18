# -*- coding: utf-8 -*-
"""
Задание 18.2b
"""
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml
import re
def send_config_commands(device, config_commands, log=False):
    error_command = ["Invalid input detected", "Incomplete command", "Ambiguous command"]
    good_result = []
    bad_result = []
    try:
        if log:
            print(f"Подключаюсь к {device['host']}...")
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in config_commands:
                prompt = ssh.find_prompt()
                prompt_after_command = ssh.send_config_set(command)
                if "% " in prompt_after_command:
                    regex = r"% .+"
                    match = re.findall(regex, prompt_after_command)
                    command_error = [x for x in error_command if x in match[0]][:1]#[:1]-означает что если ничего не найдено ошибки не будет, если использовать [0] то будет ошибка, match[0] - все что совпаде регулярном выражении
                    print(f"Команда {command} выполнилась с ошибкой \"{command_error[0]}\" на устройстве {device['host']}")
                    bad_result.append(command)
                else:
                    good_result.append(command)
        print(" This is a list of good commands = ", good_result,"\n","This is a list of bad commands = ", bad_result, "\n")
        return good_result, bad_result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)

if __name__ == "__main__":
    #commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]#correct
    commands = ["logging 910.255.255.1", "a", "no logging sole", "no logging console"]#wrong
    with open("page471_Task18_OTVET_devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_config_commands(dev, commands, log=True))