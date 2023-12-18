# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 314
# Task 12.2
## convert_ranges_to_ip_list
## ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
## ['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
## '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']
import ipaddress
def convert_ranges_to_ip_list(list_of_ip):
    ip_list_in_function = []
    for ip in list_of_ip:
        try:
            ip_real = ipaddress.ip_address(ip)
            ip_list_in_function.append(ip)
        except:
            if "-" in ip:
                ip = list(str(ip).split("-"))
                try:
                    ip_first = ipaddress.ip_address(ip[0])
                    ip_list_in_function.append(ip[0])
                    try:
                        ip_last = ipaddress.ip_address(ip[-1])
                        ip_last_list = list(str(ip_last).split("."))
                        ip_first_list = list(str(ip_first).split("."))
                        ip_diff = int(ip_last_list[-1]) - int(ip_first_list[-1])
                        j = 0
                        while j != ip_diff:
                            j += 1
                            ip_first += 1
                            ip_list_in_function.append(str(ip_first).replace("IPv4Address('","").replace("')",""))
                    except:
                        if ip[-1].isdigit():
                            ip_first_list = list(str(ip_first).split("."))
                            ip_diff = int(ip[-1]) - int(ip_first_list[-1])
                            i = 0
                            while i != ip_diff:
                                i += 1
                                ip_first += 1
                                ip_list_in_function.append(str(ip_first).replace("IPv4Address('","").replace("')",""))
                        else:
                            pass
                except:
                    pass
    result = tuple(ip_list_in_function)
    return result
if __name__ == "__main__":
    ip_list = ['8.8.4.4', '1.1.1.1-3', '9.9.9.9', '172.21.41.128-172.21.41.132', '8.8.8.8']
    print(convert_ranges_to_ip_list(ip_list))