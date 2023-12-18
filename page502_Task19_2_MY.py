# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
команду show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя текстового файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в обычный текстовый файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):
R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down
Для выполнения задания можно создавать любые дополнительные функции.
Проверить работу функции на устройствах из файла devices.yaml
"""
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from datetime import datetime
import time
from itertools import repeat
import logging
import yaml
from netmiko import ConnectHandler, NetMikoAuthenticationException

logging.getLogger('paramiko').setLevel(logging.WARNING)
logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO,
    )
def send_show(device_dict, command):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received: {}'
    ip = device_dict['host']
    logging.info(start_msg.format(datetime.now().time(), ip))
    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            prompt = ssh.find_prompt()
            prompt_command = prompt + command
            result = ssh.send_command(command)
            logging.info(received_msg.format(datetime.now().time(), ip))
        return {prompt_command:result}
    except NetMikoAuthenticationException as err:
        logging.warning(err)

def end_show_command_to_devices(devices, command, filename, limit=3):
    data = {}
    clear_file = open(filename, 'w')
    clear_file.close()
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(send_show, devices, repeat(command))
        for device, output in zip(devices, result):
            for prompt_command, output_command in output.items():
                print(device['host'],"\n",prompt_command,"\n",output_command,"\n")
                with open(filename,'a') as file:
                    print_to_file = f"{device['host']}\n{prompt_command}\n{output_command}\n\n"
                    file.write(print_to_file)

if __name__ == "__main__":
    with open('page502_19_devices_correct.yaml') as f:
        devices = yaml.safe_load(f)
        pprint(end_show_command_to_devices(
            devices, 'sh ip int br', 'page502_19_task2_MY_result.txt'
        ))