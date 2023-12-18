# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 377
# Task 15.5
#"Eth 0/0": "description Connected to SW1 port Eth 0/1"
import re
def generate_description_from_cdp(sh_cdp_neighbors):
    with open(sh_cdp_neighbors) as file:
        dict_all = {}
        for line in file:
            regex = r'(?P<Device_ID>^[A-Z,a-z,-,_,0,1-9]+[^>])\s+(?P<Local_Intrf>\S+ \S+)\s+[A-Z,1-9,\s,]+\s+(?P<Port_ID>\S+ \S+$)'
            match = re.search(regex, line)
            if match:
                device_id = str(match.group('Device_ID'))
                port_id = str(match.group('Port_ID'))
                local_string = f'description Connected to {device_id}port {port_id}'
                dict_all[match.group('Local_Intrf')] = local_string
        return dict_all
if __name__ == "__main__":
    print(generate_description_from_cdp('page377_sh_cdp_n_sw1.txt'))