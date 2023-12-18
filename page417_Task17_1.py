# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 417
# Task 17.1
import csv
import re
def write_dhcp_snooping_to_csv(filenames, output):
    headers = ['switch', 'mac', 'ip', 'vlan', 'interface']
    list_all = []
    list_all.append(headers)
    regex_hostname = (r'^\S+_(?P<hostname>\S+)_dhcp\S+')
    match_hostname = re.search(regex_hostname, filenames)
    hostname = match_hostname.group('hostname')
    with open(filenames, 'r') as src, open(output, 'w') as dst:
        regex = (r'(?P<mac>^\S+[0-9,a-f,A-F,:])\s+'
                 r'(?P<ip>\S+[0-9,.])\s+\S+\s+\S+\s+'
                 r'(?P<vlan>\d+)\s+'
                 r'(?P<interface>\S+$)')
        for line in src:
            match = re.search(regex, line)
            if match:
                list_local = [hostname, match.group('mac'), match.group('ip'), match.group('vlan'), match.group('interface')]
                list_all.append(list_local)
        writer = csv.writer(dst)
        writer.writerows(list_all)
if __name__ == '__main__':
    write_dhcp_snooping_to_csv('page417_sw1_dhcp_snooping.txt', 'page417_task1_output.csv')