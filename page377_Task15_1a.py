# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 377
# Task 15.1a
# example [("10.0.1.1", "255.255.255.0"), ("10.0.2.1", "255.255.255.0")]
import re
def get_ip_from_cfg(filename_with_config):
    with open(filename_with_config) as file:
        match1 = re.findall(r'interface(?P<port> \S+)\n(?:(?:.*\n*){0,5}) ip address (?P<ip>\S+) (?P<mask>\S+)\n(?:(?:.*\n*){0,5})!\n', file.read())
        dict_all = {}
        for port, ip, mask in match1:
            dict_all[port] = ip, mask
    return dict_all
if __name__ == "__main__":
    print(get_ip_from_cfg('page377_config_r1.txt'))