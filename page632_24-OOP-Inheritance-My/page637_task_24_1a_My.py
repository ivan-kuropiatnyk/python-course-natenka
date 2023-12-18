# -*- coding: utf-8 -*-
"""
Задание 24.1a

Скопировать и дополнить класс CiscoSSH из задания 24.1.

Перед подключением по SSH необходимо проверить если ли в словаре с параметрами
подключения такие параметры: username, password, secret.
Если какого-то параметра нет, запросить значение у пользователя, а затем выполнять
подключение. Если все параметры есть, выполнить подключение.

In [1]: from task_24_1a import CiscoSSH

In [2]: device_params = {
   ...:         'device_type': 'cisco_ios',
   ...:         'host': '192.168.100.1',
   ...: }

In [3]: r1 = CiscoSSH(**device_params)
Введите имя пользователя: cisco
Введите пароль: cisco
Введите пароль для режима enable: cisco

In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                190.16.200.1    YES NVRAM  up                    up
Ethernet0/3                192.168.230.1   YES NVRAM  up                    up
Ethernet0/3.100            10.100.0.1      YES NVRAM  up                    up
Ethernet0/3.200            10.200.0.1      YES NVRAM  up                    up
Ethernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '
"""
from page637_task_24_base_connect_class_My import BaseSSH
import time

class CiscoSSH(BaseSSH):
    print(BaseSSH)
    def __init__(self, **device_params):
        '''list_args = ['ip', 'username', 'password', 'device_type', 'secret']
        for arg in list_args:
            arg = arg.replace("\'","").replace("\"","")
            if not arg:
                f"{arg}" = input(f"Please enter the value for {arg} = ")
        '''
        dict_params = {'ip': None,
                       'username': None,
                       'password': None,
                       'device_type': None,
                       'secret': None
                       }
        for key, value in device_params.items():
            if key in list(dict_params) and value != None and len(value) > 0:
                dict_params[key] = value
            else:
                dict_params[key] = input(f"enter {key}:")
        if None in list(dict_params.values()):
            index = 0
            for value in list(dict_params.values()):
                index += 1
                if value == None:
                    dict_params[list(dict_params)[index - 1]] = input(f"enter {list(dict_params)[index - 1]}:")
        device_params.clear()
        device_params = dict_params
        super().__init__(**device_params)
        self.ssh.enable()
        time.sleep(1)
if __name__ == "__main__":
    #r1 = CiscoSSH(ip = '172.17.20.41', username = 'ivankurop', password = 'qweszxc', device_type = 'cisco_ios', secret = 'qweszxc')
    r1 = CiscoSSH(ip = '172.17.20.41',
                  username = 'ivankurop',
                  device_type = 'cisco_ios')
    print(r1.send_show_command('sh clock'))