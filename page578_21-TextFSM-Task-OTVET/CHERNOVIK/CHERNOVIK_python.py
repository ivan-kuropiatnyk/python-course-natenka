import subprocess as sp
#print(sp.check_output('ping -c 2 -n 8.8.8.8', shell=True))

result3 = subprocess.run(['ping', '-c', '1', '-n', '8.8.8.8'])
print(result3)

# Работа со стандартным потоком ошибок
result8 = subprocess.run(['ping', '-c', '3', '-n', 'a'], stderr=subprocess.PIPE, encoding='utf-8')
print("\n result 8 =>\n", result8.stdout)
print("\n result 8 =>\n", result8.stderr)

# Примеры использования модуля
reply = subprocess.run(['ping', '-c', '1', '-n', '8.8.8.8'])
if reply.returncode == 0:
    print('Alive')
else:
    print('Unreachable')


def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
    * True
    * command output (stdout)
    On failure:
    * False
    * error output (stderr)
    """
    reply = subprocess.run(['ping', '-c', '1', '-n', ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stderr


print(ping_ip('8.8.8.8'))
print(ping_ip('a'))


# Task 12.1
import subprocess
from datetime import datetime
import time
list_of_ip1 = ['8.8.8.8', '172.17.30.205', '8.8.4.4', '172.17.20.192', '172.17.30.254', '172.17.20.161', '172.17.20.167',
              '172.17.30.1']
list_of_ip2 = ['8.8.8.8', '172.17.30.205', '8.8.4.4', '172.17.30.206', '172.17.30.254']
def ping_ip_addresses(list_of_ip_to_ping):
    list_of_alive_ip = []
    list_of_unreachable_ip = []
    list_of_wrong_ip = []
    for ip in list_of_ip_to_ping:
        ping = subprocess.run(['ping', '-c', '1', '-n', ip],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              encoding='utf-8')
        if ping.returncode == 0:
            list_of_alive_ip.append(ip)
        else:
            list_of_unreachable_ip.append(ip)
    return list_of_alive_ip, list_of_unreachable_ip
if __name__ == "__main__":
    print(ping_ip_addresses(list_of_ip1))

12.7 Задания ОТВЕТ
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess


def ping_ip_addresses(ip_addresses):
    reachable = []
    unreachable = []
    for ip in ip_addresses:
        result = subprocess.run(
            ["ping", "-c", "3", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    return reachable, unreachable


if __name__ == "__main__":
    print(ping_ip_addresses(["10.1.1.1", "8.8.8.8"]))


#Если указать его при вызове функции run, результат будет получен в виде строки:
result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'],
stdout=subprocess.PIPE, encoding='utf-8')
result.stdout

#Параметр timeout_ops указывает сколько ждать выполнения команды:
ssh.send_command("ping 8.8.8.8", timeout_ops=20)

reply = ssh.send_commands(["ping 192.168.100.2", "sh clck", "sh ip int br"], stop_on_failed=True)