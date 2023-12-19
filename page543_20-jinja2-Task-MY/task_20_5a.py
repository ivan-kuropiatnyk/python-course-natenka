# -*- coding: utf-8 -*-
"""
Задание 20.5a

Создать функцию configure_vpn, которая использует
шаблоны из задания 20.5 для настройки VPN на маршрутизаторах
на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству 1
* dst_device_params - словарь с параметрами подключения к устройству 2
* src_template - имя файла с шаблоном, который создает конфигурацию для строны 1
* dst_template - имя файла с шаблоном, который создает конфигурацию для строны 2
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов
и данных на каждом устройстве с помощью netmiko.
Функция возвращает кортеж с выводом команд с двух
маршрутизаторов (вывод, которые возвращает метод netmiko send_config_set).
Первый элемент кортежа - вывод с первого устройства (строка),
второй элемент кортежа - вывод со второго устройства.

При этом, в словаре data не указан номер интерфейса Tunnel,
который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel,
взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 5.
И надо будет настроить интерфейс Tunnel 5.

Для этого задания тест проверяет работу функции на первых двух устройствах
из файла devices.yaml. И проверяет, что в выводе есть команды настройки
интерфейсов, но при этом не проверяет настроенные номера тунелей и другие команды.
Они должны быть, но тест упрощен, чтобы было больше свободы выполнения.
"""
import yaml
import re
from task_20_1 import generate_config
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

def configure_vpn(
    src_device_params,
    dst_device_params,
    src_template,
    dst_template,
    vpn_data_dict):

    show_command = "sh ip int br | inc unnel"
    devices = [src_device_params, dst_device_params]
    occupied_tun_num = []

    # SHOW COMMAND AND DEFINE NUMBER OF TUNNEL
    for device in devices:
        try:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                show_output = ssh.send_command(show_command)
                if show_output:
                    regex = r"Tunnel(?P<num_tunnel>\d+)\s"
                    tun_num = [
                        occupied_tun_num.append(int(match.group('num_tunnel')))
                        for match in re.finditer(regex, show_output)
                    ]
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)

    if occupied_tun_num:
        vpn_data_dict["tun_num"] = max(occupied_tun_num) + 1
    else:
        vpn_data_dict["tun_num"] = 0
    print("The Configured Tunnel Numbers will be: ", vpn_data_dict["tun_num"])

    # GENERATE CONFIG
    src_config = generate_config(src_template, vpn_data_dict)
    dst_config = generate_config(dst_template, vpn_data_dict)

    # ENTER GENERATED CONFIG
    for device in devices:
        print("connecting to CONFIGURE ===>", device['host'])
        try:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                prompt = ssh.find_prompt()
                if device['host'] == vpn_data_dict["wan_ip_1"]:
                    result_src = ssh.send_config_set(src_config.split("\n"))
                    print(result_src)
                else:
                    result_dst = ssh.send_config_set(dst_config.split("\n"))
                    print(result_dst)
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print(error)
        print(device['host'], "<===End CONFIGURATION")

if __name__ == "__main__":
    template1 = "templates/gre_ipsec_vpn_1.txt"
    template2 = "templates/gre_ipsec_vpn_2.txt"

    data = {
        "tun_num": None,
        "wan_ip_1": "172.17.20.41",
        "wan_ip_2": "172.17.20.4",
        "tun_ip_1": "10.41.4.17 255.255.255.252",
        "tun_ip_2": "10.41.4.18 255.255.255.252",
    }

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        r1 = devices[0]
        r2 = devices[-1]
    configure_vpn(r1, r2, template1, template2, data)