# -*- coding: utf-8 -*-

"""
Задание 22.2

Создать класс CiscoTelnet, который подключается по Telnet к оборудованию Cisco.

При создании экземпляра класса, должно создаваться подключение Telnet, а также
переход в режим enable.
Класс должен использовать модуль telnetlib для подключения по Telnet.

У класса CiscoTelnet, кроме __init__, должно быть, как минимум, два метода:
* _write_line - принимает как аргумент строку и отправляет на оборудование строку
  преобразованную в байты и добавляет перевод строки в конце. Метод _write_line должен
  использоваться внутри класса.
* send_show_command - принимает как аргумент команду show и возвращает вывод
  полученный с обрудования

Параметры метода __init__:
* ip - IP-адрес
* username - имя пользователя
* password - пароль
* secret - пароль enable

Пример создания экземпляра класса:
In [2]: from task_22_2 import CiscoTelnet

In [3]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}
   ...:

In [4]: r1 = CiscoTelnet(**r1_params)

In [5]: r1.send_show_command("sh ip int br")
Out[5]: 'sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
Ethernet0/2                unassigned      YES manual up                    up
Ethernet0/3                192.168.130.1   YES NVRAM  up                    up
R1#'


Подсказка:
Метод _write_line нужен для того чтобы можно было сократить строку:
self.telnet.write(line.encode("utf-8") + b"
")

до такой:
self._write_line(line)

Он не должен делать ничего другого.
"""
import telnetlib
import time
from pprint import pprint
'''
def to_bytes(line):
    
    #выполняет преобразование в байты и добавление перевода строки
    
    return f"{line}\n".encode("utf-8")
'''

class CiscoTelnet:
    def __init__(self, parameters):
        self.ip = parameters['ip']
        self.username = parameters['username']
        self.password = parameters['password']
        self.secret = parameters['secret']
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

    def info(self):#необязательная функция, ввел ее чтоб облегчить траблшутинг
        print(f"IP={self.ip}\nUSERNAME={self.username}\nPASSWORD={self.password}\nSECRET={self.secret}")

    def _write_line(self, line):
        '''
            выполняет преобразование в байты и добавление перевода строки
            в предыдущих заданиях это та же функция что и to_bytes(line)
            '''
        return f"{line}\n".encode("utf-8")

    def send_show_command(self, commands):
        result = {}
        for command in commands:
            self.telnet.write(self._write_line(command))
            output = self.telnet.read_until(b"#", timeout=5).decode("utf-8")
            result[command] = output.replace("\r\n", "\n")
        return result

if __name__ == "__main__":
    r1_params = {
        'ip': '172.17.20.41',
        'username': 'ivankurop',
        'password': 'qweszxc',
        'secret': 'qweszxc'}
    commands = ["sh ip int br", "sh arp"]
    r1 = CiscoTelnet(r1_params)
    print(r1.send_show_command(commands))
    #print(r1.info())
