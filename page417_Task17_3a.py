# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 417
# Task 17.3a
import glob
import yaml
from page417_Task17_3 import parse_sh_cdp_neighbors
def generate_topology_from_cdp(list_of_files, save_to_filename='None'):
    dict_all = {}
    for filename in list_of_files:
        with open(filename, 'r') as source_file:
            file_content_one_line = source_file.read()
            dict_local = parse_sh_cdp_neighbors(file_content_one_line)
            for key, value in dict_local.items():
                dict_all[key] = value
    if save_to_filename:
        with open(save_to_filename, 'w') as destination_file:
            yaml.dump(dict_all, destination_file)
    return dict_all
if __name__ == "__main__":
    sh_cdp_files = glob.glob("page417_sh_cdp*.txt")
    print(generate_topology_from_cdp(sh_cdp_files, "page_417_topology.yaml"))