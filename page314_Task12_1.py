# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 314
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