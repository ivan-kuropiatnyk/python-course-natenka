'''
Python for network engineers Natasha Samoilenko
'''
# Page range 286
# Task 11.2a
import sys
from page285_Task_11_1 import parse_cdp_neighbors
from draw_network_graph import apply_styles
from draw_network_graph import draw_topology



def unique_network_map(filenames):
    count = 0
    dict_result = {}
    for file in filenames:
        count += 1
        with open(file) as f:
            parsed = parse_cdp_neighbors(f.read())
            for device_source, device_dest in parsed.items():
                if dict_result.get(device_source) == None and dict_result.get(device_dest) == None:
                    dict_result[device_source] = device_dest
                elif dict_result.get(device_source) != dict_result.get(device_source) and dict_result.get(device_dest) == None:
                    dict_result[device_source] = device_dest
            if len(filenames) == count:
                return dict_result



if __name__ == "__main__":
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]

    print(unique_network_map(infiles))
    dict_result2 = unique_network_map(infiles)
    draw_topology(dict_result2)