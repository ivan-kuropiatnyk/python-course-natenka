# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 374
# Task 15.1
# example [("10.0.1.1", "255.255.255.0"), ("10.0.2.1", "255.255.255.0")]
import re
def get_ip_from_cfg(filename_with_config):
    with open(filename_with_config) as file:
        config = file.read()
        regex = r' ip address (\S+) (\S+)'
        match = re.findall(regex, config)
    return match

if __name__ == "__main__":
    print(get_ip_from_cfg('page377_config_r1.txt'))