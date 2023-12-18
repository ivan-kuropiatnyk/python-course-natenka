# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping_one_ip(ip):
    result = subprocess.run(
        ["ping", "-c", "2", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        )
    return {ip:result.returncode}
def ping_ip_addresses(ip_list, limit):
    reachable_list = []
    unreachable_list = []
    data = {}
    with ThreadPoolExecutor(max_workers=limit) as executor:
        future_ping = [
            executor.submit(ping_one_ip, ip) for ip in ip_list
        ]
        for f in as_completed(future_ping):
            result = f.result()
            data.update(result)
    for key, value in data.items():
        if value == 0:
            reachable_list.append(key)
        elif value != 0:
            unreachable_list.append(key)
    return reachable_list, unreachable_list

if __name__ == '__main__':
    ip_list = ["10.1.1.1", "8.8.8.8", "172.17.20.4", "172.17.20.41", "172.17.20.42", "172.17.20.43"]
    print(ping_ip_addresses(ip_list, 4))