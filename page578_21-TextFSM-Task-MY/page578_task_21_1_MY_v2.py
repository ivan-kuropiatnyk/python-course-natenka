# -*- coding: utf-8 -*-
"""
Задание 21.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды sh ip int br с оборудования
и шаблоне templates/sh_ip_int_br.template.

"""
from netmiko import ConnectHandler
import textfsm
from tabulate import tabulate
def parse_command_output(template, command_output):
    with open(template) as templ:
        fsm = textfsm.TextFSM(templ)  # - класс, который обрабатывает шаблон и создает из него объект в TextFSM
        header = fsm.header
        parsed = fsm.ParseText(command_output)
        result = tabulate(parsed, headers=header)
    #print(fsm)
    return result

# вызов функции должен выглядеть так
if __name__ == "__main__":

    r1_params = {
    "device_type": "cisco_ios",
    "host": "172.17.20.41",
    "username": "ivankurop",
    "password": "qweszxc",
    "secret": "qweszxc",
    }
    with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")

    template = "templates/sh_ip_int_br.template"
    #file_output = "output/sh_ip_int_br.txt"
    #output = open(file_output).read()
    result = parse_command_output(template, output)
    print(result)