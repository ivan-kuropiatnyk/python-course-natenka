# -*- coding: utf-8 -*-

"""
Задание 22.2c

Скопировать класс CiscoTelnet из задания 22.2b и изменить метод send_config_commands
добавив проверку команд на ошибки.

У метода send_config_commands должен быть дополнительный параметр strict:
* strict=True значит, что при обнаружении ошибки, необходимо сгенерировать
  исключение ValueError (значение по умолчанию)
* strict=False значит, что при обнаружении ошибки, надо только вывести
  на стандартный поток вывода сообщене об ошибке

Метод дожен возвращать вывод аналогичный методу send_config_set
у netmiko (пример вывода ниже). Текст исключения и ошибки в примере ниже.

Пример создания экземпляра класса:
In [1]: from task_22_2c import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
In [6]: commands = commands_with_errors+correct_commands

Использование метода send_config_commands:

In [7]: print(r1.send_config_commands(commands, strict=False))
При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.
При выполнении команды "logging" на устройстве 192.168.100.1 возникла ошибка -> Incomplete command.
При выполнении команды "a" на устройстве 192.168.100.1 возникла ошибка -> Ambiguous command:  "a"
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"
R1(config)#logging buffered 20010
R1(config)#ip http server
R1(config)#end
R1#

In [8]: print(r1.send_config_commands(commands, strict=True))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-0abc1ed8602e> in <module>
----> 1 print(r1.send_config_commands(commands, strict=True))

...

ValueError: При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.

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

    def send_config_command(self, conf_commands, strict=False):
        result = {}
        good_result = {}
        bad_result = {}
        self.telnet.write(self._write_line('conf t'))
        output = self.telnet.read_until(b"#", timeout=5).decode("utf-8")
        result['conf t'] = output.replace("\r\n", "\n")
        for command in conf_commands:
            self.telnet.write(self._write_line(command))
            output = self.telnet.read_until(b"#", timeout=5).decode("utf-8")
            result[command] = output.replace("\r\n", "\n")
            count_n = result[command].count('\n')#посчитаем количество переносов строки, если их больше одного, то результат команды с ошибкой
            if count_n > 1:
                bad_result[command] = result[command]
                if strict == True:
                    raise ValueError(
                        f"При выполнении команды {command} на устройстве {self.ip} возникла ошибка "
                        f"\n-> Invalid input detected at '^' marker."
                    )
            elif count_n == 1:
                good_result[command] = result[command]
            else:
                bad_result[command] = "Result is strange:"+result[command]
        self.telnet.write(self._write_line('end'))
        output = self.telnet.read_until(b"#", timeout=5).decode("utf-8")
        result['end'] = output.replace("\r\n", "\n")
        print("\n", result, "\n\n", good_result, "\n\n", bad_result, "\n\n")
        return result, good_result, bad_result

if __name__ == "__main__":
    dev_name_in_class = []#так как имена экземпляров должны отличаться, тут будут имена переменных экземпляров для класса, к примеру device1, device2
    count_for = 0#считает количество циклов, передавая номер каждого цикла в имя переменной
    full_pth = os.path.join(os.getcwd(), "templates")
    #configuration = [ 'logging 10.1.1.1', 'interface loop55', 'ip address 5.5.5.5 255.255.255.255']
    configuration = ['logging 10.1.1.1','logVIging 10.1.1.1', 'interface loGop55', 'ip address 5.5.5.5 255.255.255.255']
    with open("page596_task_22_JustOneDevice.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        count_for += 1
        dev_name = "dev" + str(count_for)#создает имя экземпляра класса в зависимости от номера итерации, или же номера устройства в файле YAML
        dev_name_in_class.append(dev_name)
        commands = ["sh ip int br", "sh clock"]
        dev_name_in_class[-1] = CiscoTelnet(dev)
        dev_name_in_class[-1].send_config_command(configuration,strict=False)