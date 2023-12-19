# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 377
# Task 15.2
'''
[("FastEthernet0/0", "10.0.1.1", "up", "up"),
("FastEthernet0/1", "10.0.2.1", "up", "up"),
("FastEthernet0/2", "unassigned", "down", "down")]
'''
import re
def parse_sh_ip_int_br(filename):
    list_all = []
    regex = (r'(?P<interface>\S+\d) '
             r'\s+(?P<ip>\S+)'
             r'\s+\S+\s+\S+\s+(?P<status>([a]\S+ \S+)|(\S+))\s+'
             r'(?P<protocol>\S+$)')
    with open(filename) as file:
        for line in file:
            match = re.search(regex, line)
            if match:
                local_tuple = match.group('interface'), match.group('ip'), match.group('status'), match.group('protocol')
                list_all.append(local_tuple)
    return list_all
if __name__ == "__main__":
    print(parse_sh_ip_int_br('page377_sh_ip_int_br.txt'))