# -*- coding: utf-8 -*-
"""
Задание 19.3

Создать функцию send_command_to_devices, которая отправляет разные
команды show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять
  какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом
команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh int desc
Interface                      Status         Protocol Description
Et0/0                          up             up
Et0/1                          up             up
Et0/2                          admin down     down
Et0/3                          admin down     down
Lo9                            up             up
Lo19                           up             up
R3#sh run | s ^router ospf
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
"""
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml
from datetime import datetime
import time
import logging

logging.getLogger('paramiko').setLevel(logging.WARNING)
logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO,
    )

def send_show_command(device, commands):
    result = {}
    commands_sent = []
    ip_add = device['host']
    commands_list = commands[ip_add]
    commands_sent.append(commands_list)
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received: {}'
    logging.info(start_msg.format(datetime.now().time(), ip_add))
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            prompt = ssh.find_prompt()
            for command in commands_sent:
                output = ssh.send_command(command)
                logging.info(received_msg.format(datetime.now().time(), ip_add))
                prompt_command = prompt + command
                result[prompt_command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)

def send_command_to_devices(devices, commands_dict, filename, limit=3):
    clear_file = open(filename, 'w')
    clear_file.close()
    with open(devices) as f:
        output_devices = yaml.safe_load(f)
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(send_show_command, output_devices, repeat(commands_dict))
        for device, output in zip(output_devices, result):
            for prompt_command, output_command in output.items():
                print(device['host'],"\n",prompt_command,"\n",output_command,"\n")
                with open(filename,'a') as file:
                    print_to_file = f"{device['host']}\n{prompt_command}\n{output_command}\n\n"
                    file.write(print_to_file)

if __name__ == "__main__":
    commands = {
        "172.17.20.41": "sh ip int br",
        "172.17.20.42": "sh arp",
        "172.17.20.43": "sh ip int br",
    }
    devices = "page502_19_devices_correct.yaml"
    filename = 'page502_19_task3_MY_result.txt'
    send_command_to_devices(devices, commands, filename, limit=2)