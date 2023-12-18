# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 377
# Task 15.3
#ip nat inside source static tcp 10.1.2.63 80 interface GigabitEthernet0/1 80
import re
def convert_ios_nat_to_asa(nat_ios, nat_asa):
    with open(nat_ios) as src, open(nat_asa, 'w') as dst:
        regex = r'ip nat inside source static tcp (?P<ip>\S+) (?P<p1>\S+) interface \S+ (?P<p2>\S+)'
        for line in src:
            match = re.search(regex, line)
            template = f"object network LOCAL_{match.group('ip')}\n host {match.group('ip')}\n nat (inside,outside) static interface service tcp {match.group('p1')} {match.group('p2')}\n"
            dst.write(template)
if __name__ == "__main__":
    convert_ios_nat_to_asa('page377_cisco_nat_config.txt', 'page377_cisco_nat_asa.txt')