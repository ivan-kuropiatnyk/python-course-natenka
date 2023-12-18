'''
Python for network engineers Natasha Samoilenko
'''
# Page range 278 - 284
# 11. Модули
## Импорт модуля
### В Python есть несколько способов импорта модуля:
### • import module
### • import module as
### • from module import object
### • from module import *

print(dir())
import os
print(dir())
print(os.getlogin())

import subprocess as sp
#print(sp.check_output('ping -c 2 -n 8.8.8.8', shell=True))

from os import getlogin, getcwd
print(getcwd())
print(getlogin())

from os import *
print(dir())
print(len(dir()))

##11.2 Создание своих модулей
import ipaddress
def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False
ip1 = '10.1.1.1'
ip2 = '10.1.1'
print('Проверка IP...')
print(ip1, check_ip(ip1))
print(ip2, check_ip(ip2))
print(dir())

from check_ip_function import check_ip
def return_correct_ip(ip_addresses):
    correct = []
    for ip in ip_addresses:
        if check_ip(ip):
            correct.append(ip)
    return correct
print('Проверка списка IP-адресов')
ip_list = ['10.1.1.1', '8.8.8.8', '2.2.2']
correct = return_correct_ip(ip_list)
print(correct)

print(list(filter(check_ip, ip_list)))
print([ip for ip in ip_list if check_ip(ip)])
list_ip=['10.1.1.1', '8.8.8.8']
def return_correct_ip(ip_addresses):
    return [ip for ip in ip_addresses if check_ip(ip)]
print(return_correct_ip(list_ip))

#if __name__ == "__main__"
##все строки, которые находятся в блоке if __name__ == '__main__' не выполняются при импорте.
##То есть, условие if __name__ == '__main__' проверяет, был ли файл
##запущен напрямую.
##Как правило, в блок if __name__ == '__main__' заносят все вызовы функций и вывод ин-
##формации на стандартный поток вывода.
import ipaddress
def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False
if __name__ == '__main__':
    ip1 = '10.1.1.1'
    ip2 = '10.1.1'
    print('Проверка IP...')
    print(ip1, check_ip(ip1))
    print(ip2, check_ip(ip2))

from check_ip_function import check_ip
def return_correct_ip(ip_addresses):
    correct = []
    for ip in ip_addresses:
        if check_ip(ip):
            correct.append(ip)
    return correct
print('Проверка списка IP-адресов')
ip_list = ['10.1.1.1', '8.8.8.8', '2.2.2']
correct = return_correct_ip(ip_list)
print(correct)

#Пути поиска модулей
##Содержимое sys.path состоит из:
##• текущего каталога
##• каталогов, которые указаны в переменной PYTHONPATH
##• пути по умолчанию (зависят от установки Python)
import sys
print(sys.path)
