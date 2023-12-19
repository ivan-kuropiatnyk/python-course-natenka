# -*- coding: utf-8 -*-

"""
Задание 24.2c

Скопировать класс MyNetmiko из задания 24.2b.
Проверить, что метод send_command кроме команду, принимает еще и дополнительные
аргументы, например, strip_command.

Если возникает ошибка, переделать метод таким образом, чтобы он принимал
любые аргументы, которые поддерживает netmiko.


In [2]: from task_24_2c import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br', strip_command=False)
Out[4]: 'sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                190.16.200.1    YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up
Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up
Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

In [5]: r1.send_command('sh ip int br', strip_command=True)
Out[5]: 'Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                190.16.200.1    YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up
Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up
Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

"""
from netmiko.cisco.cisco_ios import CiscoIosSSH
import re

class ErrorInCommand(Exception):
    """
    Исключение генерируется, если при выполнении команды на оборудовании, возникла ошибка.
    """

class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, result):
        error_message = 'Команда \"{cmd}\" выполнилась с ошибкой \"{error}\" на устройстве \"{ip}\"'
        regex = "% (?P<errmsg>.+)"
        error_in_result = re.search(regex, result)
        if error_in_result:
            raise ErrorInCommand(
                error_message.format(
                    cmd=command, ip = self.host, error=error_in_result.group("errmsg")
                )
            )

    def send_command(self, command, *args, **kwargs):
        output = super().send_command(command)
        self._check_error_in_command(command, output)
        return output

    def send_config_set(self, **kwargs):
        if type(kwargs['config_commands']) != list:
            make_list = kwargs['config_commands']
            kwargs['config_commands'] = [make_list]
        for command in kwargs['config_commands']:
            output = super().send_config_set(command, exit_config_mode=False)
            error = self._check_error_in_command(command, output)
            if error:
                break
            else:
                print(output)

if __name__ == "__main__":
    device_params = {
        "device_type": "cisco_ios",
        "ip": "172.17.20.41",
        "username": "ivankurop",
        "password": "qweszxc",
        "secret": "qweszxc",
    }
    r1 = MyNetmiko(**device_params)
    #print(r1.send_command('sh sh'))
    r1.send_config_set(config_commands=['ntp logging', 'ntp server 10.0.0.3'], strip_command=False)