# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 377
# Task 15.4
#ip nat inside source static tcp 10.1.2.63 80 interface GigabitEthernet0/1 80
import re
def get_ints_without_description(config_file):
    with open(config_file) as file:
        config = file.read()
        regex = r'(?:interface (\S+\d)\n)(?!(?: description \S+))'
        match = re.findall(regex, config)
        return match
if __name__ == "__main__":
    print(get_ints_without_description('page377_config_r1.txt'))