# -*- coding: utf-8 -*-

"""
Задание 22.2a
"""
import telnetlib
import time
from pprint import pprint
import os
from textfsm import clitable
import yaml

'''
def to_bytes(line):

    #выполняет преобразование в байты и добавление перевода строки

    return f"{line}\n".encode("utf-8")
'''


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

    def send_show_command(self, commands, parse=False):
        result = {}
        for command in commands:
            self.telnet.write(self._write_line(command))
            output = self.telnet.read_until(b"#", timeout=5).decode("utf-8")
            if parse == False:
                print(output)
            elif parse == True:
                index_file = "index"
                templ_path = "templates"
                attributes = {"Command": command, "Vendor": self.device_type}
                cli_table = clitable.CliTable(index_file, templ_path)
                cli_table.ParseCmd(output, attributes)
                print([dict(zip(cli_table.header, row)) for row in cli_table])

if __name__ == "__main__":
    dev_name_in_class = []#так как имена экземпляров должны отличаться, тут будут имена переменных экземпляров для класса, к примеру device1, device2
    count_for = 0#считает количество циклов, передавая номер каждого цикла в имя переменной
    full_pth = os.path.join(os.getcwd(), "templates")
    with open("page596_task_22_JustOneDevice.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        count_for += 1
        dev_name = "dev" + str(count_for)#создает имя экземпляра класса в зависимости от номера итерации, или же номера устройства в файле YAML
        dev_name_in_class.append(dev_name)
        commands = ["sh ip int br", "sh clock"]
        dev_name_in_class[-1] = CiscoTelnet(dev)
        #print(dev_name_in_class[-1].info())
        dev_name_in_class[-1].send_show_command(commands, parse=True)
        dev_name_in_class[-1].send_show_command(commands, parse=False)
