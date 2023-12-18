# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 417
# Task 17.3b
"""
Создать функцию transform_topology, которая преобразует топологию в формат подходящий
для функции draw_topology.
Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.
("R1", "Eth0/0"): ("SW1", "Eth0/1")
("SW1", "Eth0/1"): ("R1", "Eth0/0")
"""
import yaml
from page417_draw_network_graph import draw_topology
def transform_topology(topo_yaml_file):
    dict_topology = {}
    with open(topo_yaml_file) as f:
        dict_yaml = yaml.safe_load(f)
        for device_local, dict1 in dict_yaml.items():
            for interface_local, dict2 in dict1.items():
                for device_remote, interface_remote in dict2.items():
                    tuple_local = (device_local, interface_local)
                    tuple_remote = (device_remote, interface_remote)
                    if dict_topology.get(tuple_remote) != tuple_local and dict_topology.get(tuple_local) != tuple_remote:
                        dict_topology[tuple_local] = tuple_remote
    draw_topology(dict_topology, out_filename="img/page417_task_17_3b_topoMY")
    return dict_topology

if __name__ == "__main__":
    print(transform_topology('page417_topology.yaml'))