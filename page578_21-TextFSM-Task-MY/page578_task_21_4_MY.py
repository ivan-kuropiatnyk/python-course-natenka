# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
import os
from pprint import pprint
from netmiko import ConnectHandler
from textfsm import clitable
import yaml

def send_and_parse_show_command(device_dict, command, templates_path):
    with ConnectHandler(**device_dict) as connection:
        connection.enable()
        device_output = connection.send_command(command)
        index_file = templates_path + '/index'
        attributes_dict = {"Command": command, "Vendor": "cisco_ios"}
        cli_table = clitable.CliTable(index_file, templates_path)
        cli_table.ParseCmd(device_output, attributes_dict)
        header = list(cli_table.header)
        #nice_table = cli_table.FormattedTable()
        result = [dict(zip(header, line)) for line in cli_table]
    return result

if __name__ == "__main__":
    full_pth = os.path.join(os.getcwd(), "templates")
    with open("page578_task_21_devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        result = send_and_parse_show_command(
            dev, "sh ip int br", templates_path=full_pth
        )
        pprint(result, width=120)