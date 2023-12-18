# -*- coding: utf-8 -*-

"""
Задание 24.2b

Скопировать класс MyNetmiko из задания 24.2a.

Дополнить функционал метода send_config_set netmiko и добавить в него проверку
на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает
вывод команд.

In [2]: from task_24_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."

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
            output = super().send_config_set(command)
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
    r1.send_config_set(config_commands=['ntp logging', 'ntp serGer 10.0.0.3'], strip_command=False)