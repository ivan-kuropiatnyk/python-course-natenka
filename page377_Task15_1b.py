# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 377
# Task 15.1b
import re
def get_ip_from_cfg(filename_with_config):
    with open(filename_with_config) as file:
        match1 = re.findall(r'interface(?P<port> \S+)(?:\n|\n(?:(?:.*\n*){0,3}))(?: ip address (?P<ip>\S+) (?P<mask>\S+)\n)(?:(?: ip address (?P<ip2>\S+) (?P<mask2>\S+) secondary\n)*)(?:(?:.*\n*){0,3})!\n', file.read())
        dict_all = {}
        for port, ip, mask, ip2, mask2 in match1:
            if ip2:
                set1 = set()
                set2 = set()
                set1.add(ip)
                set1.add(mask)
                set2.add(ip2)
                set2.add(mask2)
                set1 = tuple(set1)
                set2 = tuple(set2)
                dict_all[port] = set1, set2
            else:
                dict_all[port] = ip, mask
    return dict_all
if __name__ == "__main__":
    print(get_ip_from_cfg('page377_config_r2.txt'))