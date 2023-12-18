# -*- coding: utf-8 -*-
"""
Задание 19.3a

Создать функцию send_command_to_devices, которая отправляет список указанных
команд show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять
  какие команды. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом каждой
команды надо написать имя хоста и саму команду):

R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          87   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R1#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.30.0.1               -   aabb.cc00.6530  ARPA   Ethernet0/3.300
Internet  10.100.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.100
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down
R3#sh ip route | ex -

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
O        10.1.1.1/32 [110/11] via 192.168.100.1, 07:12:03, Ethernet0/0
O        10.30.0.0/24 [110/20] via 192.168.100.1, 07:12:03, Ethernet0/0


Порядок команд в файле может быть любым.

Для выполнения задания можно создавать любые дополнительные функции,
а также использовать функции созданные в предыдущих заданиях.

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
    #commands_sent = []
    ip_add = device['host']
    commands_list = commands[ip_add]
    #commands_sent.append(commands_list)
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received: {}'
    logging.info(start_msg.format(datetime.now().time(), ip_add))
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            prompt = ssh.find_prompt()
            for command in commands_list:
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
        "172.17.20.41": ["sh ip int br", "sh ip route | ex -"],
        "172.17.20.42": ["sh ip int br", "sh int desc"],
        "172.17.20.43": ["sh int desc"],
    }
    devices = "page502_19_devices_correct.yaml"
    filename = 'page502_19_task3a_MY_result.txt'
    send_command_to_devices(devices, commands, filename, limit=2)