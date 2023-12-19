# -*- coding: utf-8 -*-
"""
Задание 19.4

Создать функцию send_commands_to_devices, которая отправляет команду show или config
на разные устройства в параллельных потоках, а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* filename - имя файла, в который будут записаны выводы всех команд
* show - команда show, которую нужно отправить (по умолчанию, значение None)
* config - команды конфигурационного режима, которые нужно отправить (по умолчанию None)
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Аргументы show, config и limit должны передаваться только как ключевые. При передачи
этих аргументов как позиционных, должно генерироваться исключение TypeError.

In [4]: send_commands_to_devices(devices, 'result.txt', 'sh clock')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-75adcfb4a005> in <module>
----> 1 send_commands_to_devices(devices, 'result.txt', 'sh clock')

TypeError: send_commands_to_devices() takes 2 positional argument but 3 were given


При вызове функции send_commands_to_devices, всегда должен передаваться
только один из аргументов show, config. Если передаются оба аргумента, должно
генерироваться исключение ValueError.


Вывод команд должен быть записан в файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Пример вызова функции:
In [5]: send_commands_to_devices(devices, 'result.txt', show='sh clock')

In [6]: cat result.txt
R1#sh clock
*04:56:34.668 UTC Sat Mar 23 2019
R2#sh clock
*04:56:34.687 UTC Sat Mar 23 2019
R3#sh clock
*04:56:40.354 UTC Sat Mar 23 2019

In [11]: send_commands_to_devices(devices, 'result.txt', config='logging 10.5.5.5')

In [12]: cat result.txt
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.5.5.5
R1(config)#end
R1#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#logging 10.5.5.5
R2(config)#end
R2#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#logging 10.5.5.5
R3(config)#end
R3#

In [13]: commands = ['router ospf 55', 'network 0.0.0.0 255.255.255.255 area 0']

In [13]: send_commands_to_devices(devices, 'result.txt', config=commands)

In [14]: cat result.txt
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#router ospf 55
R1(config-router)#network 0.0.0.0 255.255.255.255 area 0
R1(config-router)#end
R1#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#router ospf 55
R2(config-router)#network 0.0.0.0 255.255.255.255 area 0
R2(config-router)#end
R2#
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R3(config)#router ospf 55
R3(config-router)#network 0.0.0.0 255.255.255.255 area 0
R3(config-router)#end
R3#


Для выполнения задания можно создавать любые дополнительные функции.
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
    ip_add = device['host']
    commands_list = commands[ip_add]
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

def send_config_commands(device, config_commands):
    ip_add = device['host']
    commands_list = config_commands[ip_add]
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received: {}'
    logging.info(start_msg.format(datetime.now().time(), ip_add))
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        output = ssh.send_config_set(commands_list)
        logging.info(received_msg.format(datetime.now().time(), ip_add))
    return output

def send_commands_to_devices(devices, filename, *, show=False, config=False, limit=3):
    clear_file = open(filename, 'w')
    clear_file.close()
    with open(devices) as f:
        output_devices = yaml.safe_load(f)
    try:
        if show != False and config != False:
            raise ValueError("Можно передавать только один из аргументов show/config")
        elif show == False and config == False:
            raise ValueError("No arguments was given nor show nor config")
        elif show:
            with ThreadPoolExecutor(max_workers=limit) as executor:
                result = executor.map(send_show_command, output_devices, repeat(show))
                for device, output in zip(output_devices, result):
                    for prompt_command, output_command in output.items():
                        print(device['host'],"\n",prompt_command,"\n",output_command,"\n")
                        with open(filename,'a') as file:
                            print_to_file = f"{device['host']}\n{prompt_command}\n{output_command}\n\n"
                            file.write(print_to_file)
        elif config:
            with ThreadPoolExecutor(max_workers=limit) as executor:
                result = executor.map(send_config_commands, output_devices, repeat(config))
                for device, output in zip(output_devices, result):
                    print(device['host'],"\n", output,"\n")
                    with open(filename,'a') as file:
                        print_to_file = f"{device['host']}\n{output}\n\n"
                        file.write(print_to_file)
    except (SyntaxError, TypeError):
        print('send_commands() takes just 2 positional argument')

if __name__ == "__main__":
    show_commands = {
        "172.17.20.41": ["sh ip int br", "sh ip route | ex -"],
        "172.17.20.42": ["sh ip int br", "sh int desc"],
        "172.17.20.43": ["sh int desc"],
    }
    config_commands = {
        "172.17.20.41": ["logging 10.255.255.241", "logging buffered 10241", "no logging console"],
        "172.17.20.42": ["logging 10.255.255.142", "logging buffered 10142", "no logging console"],
        "172.17.20.43": ["logging 10.255.255.43", "logging buffered 10043", "no logging console"],
    }
    devices = "page502_19_devices_correct.yaml"
    filename = 'page502_19_task4_MY_result.txt'
    filename_show = 'page502_19_task4_MY_show_result.txt'
    filename_config = 'page502_19_task4_MY_config_result.txt'
    send_commands_to_devices(devices, filename_config, config=config_commands, limit=3)
    send_commands_to_devices(devices, filename_show, show=show_commands, limit=3)
    #send_commands_to_devices(devices, filename, limit = 3)
    #send_commands_to_devices(devices, filename, show=show_commands, config=config_commands, limit=3)
    #send_commands_to_devices(devices, filename, show_commands, limit=3)
    #send_commands_to_devices(devices, filename, config_commands, 3)