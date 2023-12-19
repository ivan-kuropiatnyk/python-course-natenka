# -*- coding: utf-8 -*-
import yaml

def add_data_to_switches_table(switche_file):
    with open(switche_file) as f:
        for key1, value1 in yaml.safe_load(f).items():
            for switchname, location in value1.items():
                row = (switchname, location)
                print(type(row))

if __name__ == "__main__":
    db_filename = 'task_25_1_dhcp_snooping.db'
    switches_file = 'switches.yml'
    add_data_to_switches_table(switches_file)