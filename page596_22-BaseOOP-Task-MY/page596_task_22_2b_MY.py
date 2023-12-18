# -*- coding: utf-8 -*-

"""
Задание 22.2b

Скопировать класс CiscoTelnet из задания 22.2a и добавить метод send_config_commands.


Метод send_config_commands должен уметь отправлять одну команду конфигурационного
режима и список команд.
Метод должен возвращать вывод аналогичный методу send_config_set у netmiko
(пример вывода ниже).

Пример создания экземпляра класса:
In [1]: from task_22_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_config_commands:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.1.1.1
R1(config)#end
R1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#interface loop55
R1(config-if)#ip address 5.5.5.5 255.255.255.255
R1(config-if)#end
R1#'

"""
import telnetlib
import time
from pprint import pprint
import os
from textfsm import clitable
import yaml

class CiscoTelnet:
    def __init__(self, parameters):
        self.ip = parameters['host']
        self.username = parameters['username']
        self.password = parameters['password']
        self.secret = parameters['secret']
        self.device_type = parameters["device_type"]
        self.information = self.info()
        self.telnet = telnetlib.Telnet(self.ip)
        self.telnet.read_until(b"Username")
        self.telnet.write(self._write_line(self.username))
        self.telnet.read_until(b"Password")
        self.telnet.write(self._write_line(self.password))
        index, m, output = self.telnet.expect([b">", b"#"])
        if index == 0:
            self.telnet.write(b"enable\n")
            self.telnet.read_until(b"Password")
            self.telnet.write(self._write_line(self.secret))
            self.telnet.read_until(b"#", timeout=5)
        self.telnet.write(b"terminal length 0\n")
        self.telnet.read_until(b"#", timeout=5)
        time.sleep(3)
        self.telnet.read_very_eager()

    def info(self):  # необязательная функция, ввел ее чтоб облегчить траблшутинг
        print(f"IP={self.ip}\nUSERNAME={self.username}\nPASSWORD={self.password}\nSECRET={self.secret}")

    def _write_line(self, line):
        '''
            выполняет преобразование в байты и добавление перевода строки
            в предыдущих заданиях это та же функция что и to_bytes(line)
            '''
        return f"{line}\n".encode("utf-8")

    def send_config_command(self, conf_commands):
        result = {}
        self.telnet.write(self._write_line('conf t'))
        output = self.telnet.read_until(b"#", timeout=5).decode("utf-8")
        result['conf t'] = output.replace("\r\n", "\n")
        for command in conf_commands:
            self.telnet.write(self._write_line(command))
            output = self.telnet.read_until(b"#", timeout=5).decode("utf-8")
            result[command] = output.replace("\r\n", "\n")
        self.telnet.write(self._write_line('end'))
        output = self.telnet.read_until(b"#", timeout=5).decode("utf-8")
        result['end'] = output.replace("\r\n", "\n")
        return result

if __name__ == "__main__":
    dev_name_in_class = []#так как имена экземпляров должны отличаться, тут будут имена переменных экземпляров для класса, к примеру device1, device2
    count_for = 0#считает количество циклов, передавая номер каждого цикла в имя переменной
    full_pth = os.path.join(os.getcwd(), "templates")
    configuration = [ 'logging 10.1.1.1', 'interface loop55', 'ip address 5.5.5.5 255.255.255.255']
    with open("page596_task_22_JustOneDevice.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        count_for += 1
        dev_name = "dev" + str(count_for)#создает имя экземпляра класса в зависимости от номера итерации, или же номера устройства в файле YAML
        dev_name_in_class.append(dev_name)
        commands = ["sh ip int br", "sh clock"]
        dev_name_in_class[-1] = CiscoTelnet(dev)
        print(dev_name_in_class[-1].send_config_command(configuration))