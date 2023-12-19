# -*- coding: utf-8 -*-

"""
Задание 24.2d

Скопировать класс MyNetmiko из задания 24.2c или задания 24.2b.

Добавить параметр ignore_errors в метод send_config_set.
Если передано истинное значение, не надо выполнять проверку на ошибки и метод должен
работать точно так же как метод send_config_set в netmiko.
Если значение ложное, ошибки должны проверяться.

По умолчанию ошибки должны игнорироваться.


In [2]: from task_24_2d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#lo
% Incomplete command.

R1(config)#end
R1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#lo
% Incomplete command.

R1(config)#end
R1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

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
        if kwargs.get('ignore_errors') == False:
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
        else:
            kwargs.setdefault('ignore_errors')
            del kwargs['ignore_errors']
            output = super().send_config_set(**kwargs)
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
    #r1.send_config_set(config_commands=['ntp logging', 'ntp server 10.0.0.3'], strip_command=False)
    #r1.send_config_set(config_commands=['ntp logging', 'ntp serger 10.0.0.3'], ignore_errors=False)
    r1.send_config_set(config_commands=['ntp logging', 'ntp serger 10.0.0.3'], ignore_errors=True)