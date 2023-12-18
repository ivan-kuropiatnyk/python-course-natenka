'''
Python for network engineers Natasha Samoilenko
'''
# Page range 450-457
# 18
# 18.5 netmiko
import time
import paramiko
from netmiko import (
ConnectHandler,
NetmikoTimeoutException,
NetmikoAuthenticationException,
)
#Словарь, определяющий параметры устройствВ словаре могут указываться такие параметры:
cisco_router = {
                'device_type': 'cisco_ios',
                'host': '172.17.20.41',
                'username': 'ivankurop',
                'password': 'qweszxc',
                'secret': 'qweszxc',
                'port': 22,
                }
#Подключение по SSH
ssh = ConnectHandler(**cisco_router)
#Перейти в режим enable:
ssh.enable()
#Выйти из режима enable:
ssh.exit_enable_mode()
###В netmiko есть несколько способов отправки команд:
###• send_command - отправить одну команду
###• send_config_set - отправить список команд или команду в конфигурационном режиме
###• send_config_from_file - отправить команды из файла (использует внутри метод send_config_set)
###• send_command_timing - отправить команду и подождать вывод на основании таймера

result = ssh.send_command('show ip int br')
#####• методу можно передавать такие параметры:
#####– command_string - команда
#####– expect_string - до какой строки считывать вывод
#####– delay_factor - параметр позволяет увеличить задержку до начала поиска строки
#####– max_loops - количество итераций, до того как метод выдаст ошибку (исключение).По умолчанию 500
#####– strip_prompt - удалить приглашение из вывода. По умолчанию удаляется
#####– strip_command - удалить саму команду из вывода

##send_config_set
commands = ['router ospf 1',
'network 10.0.0.0 0.255.255.255 area 0',
'network 192.168.100.0 0.0.0.255 area 1']
result = ssh.send_config_set(commands)