# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 417
# Task 17.3
"""
R4>show cdp neighbors
Device ID Local Intrfce Holdtme Capability Platform Port ID
R5 Fa 0/1 122 R S I 2811 Fa 0/1
R6 Fa 0/2 143 R S I 2811 Fa 0/0
Функция должна вернуть такой словарь:
{"R4": {"Fa 0/1": {"R5": "Fa 0/1"},
"Fa 0/2": {"R6": "Fa 0/0"}}}
Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.
Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
def parse_sh_cdp_neighbors(sh_cdp_n):
    dict_all_cdp = {}
    dict_local = {}
    count_line = 0
    #regex_hostname = r'(?P<hostname>\S+)[^\w].*s.*cdp .*ne.*\n'#тоже работает
    regex_local_hostname = r'(?P<local_hostname>\S+)[>#].*\n'
    match_local_hostname = re.search(regex_local_hostname, sh_cdp_n)
    if match_local_hostname:
        local_hostname = match_local_hostname.group("local_hostname")
        #print(local_hostname)
    for line in sh_cdp_n.split("\n"):
        if "Device ID" in line:
            count_line += 1
        elif count_line >= 1:
            count_line += 1
            regex_cdp = (r'^(?P<remote_hostname>\S+)\s+'
                         r'(?P<local_interface>\S+\s*\S*)\s+\d+\s+(?:[A-Z]\s)+\s+\S+\s+'
                         r'(?P<remote_interface>\S+\s*\S*)'
                         )
            match_cdp = re.search(regex_cdp, line)
            if match_cdp:
                dict_remote = {}
                dict_remote[match_cdp.group('remote_hostname')] = match_cdp.group('remote_interface')
                dict_local[match_cdp.group('local_interface')] = dict_remote
                dict_all_cdp[local_hostname] = dict_local
    return dict_all_cdp

if __name__ == '__main__':
    with open("page417_sh_cdp_n_sw1.txt", 'r') as file:
        file_content_one_line = file.read()
        print(parse_sh_cdp_neighbors(file_content_one_line))