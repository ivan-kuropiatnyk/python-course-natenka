import os
import sqlite3
import re
import yaml
from create_db import create_db
from create_db import verify_file_exist

def regex_dhcp_snooping(dhcp_snooping_data_file):
    regex_dhcp_snoop_switch = re.compile(r'(?P<switch>\S+)_dhcp_snooping.txt')
    match_dhcp_snoop = regex_dhcp_snoop_switch.search(dhcp_snooping_data_file)
    if match_dhcp_snoop:
        switch_name = match_dhcp_snoop.group('switch')
    regex_dhcp_snoop = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result = []
    with open(dhcp_snooping_data_file) as data:
        for line in data:
            match_dhcp_snoop = regex_dhcp_snoop.search(line)
            if match_dhcp_snoop:
                list_match_dhcp_snoop = list(match_dhcp_snoop.groups())
                list_match_dhcp_snoop.append(switch_name)
                tuple_match_dhcp_snoop = tuple(list_match_dhcp_snoop)
                result.append(tuple_match_dhcp_snoop)
    return result

def add_data_to_dhcp_table(list_dhcp_snoop_data_files, db_file, schema_file=False):
    if not verify_file_exist(db_file):
        create_db(db_file, schema_file)
    conn = sqlite3.connect(db_file)
    for dhcp_snoop_data_file in list_dhcp_snoop_data_files:
        dhcp_snoop_data_add = regex_dhcp_snooping(dhcp_snoop_data_file)
        for row in dhcp_snoop_data_add:
            try:
                with conn:
                    query = '''insert into dhcp (mac, ip, vlan, interface, switch)
                                values (?, ?, ?, ?, ?)'''
                    conn.execute(query, row)
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)
    conn.close()

def add_data_to_switches_table(switche_file, db_file, schema_file=False):
    if not verify_file_exist(db_file):
        create_db(db_file, schema_file)
    conn = sqlite3.connect(db_file)
    with open(switche_file) as f:
        for key1, value1 in yaml.safe_load(f).items():
            for switchname, location in value1.items():
                row = (switchname, location)#creates tuple
                try:
                    with conn:
                        query = '''replace into switches (hostname, location)
                                            values (?, ?)'''
                        conn.execute(query, row)
                except sqlite3.IntegrityError as e:
                    print('Error occured: ', e)
    conn.close()

if __name__ == '__main__':
    db_filename = 'task_25_1_dhcp_snooping.db'
    schema_filename = 'dhcp_snooping_schema.sql'
    #create_db(db_filename, schema_filename)
    dhcp_snoop_file1 = 'sw1_dhcp_snooping.txt'
    dhcp_snoop_file2 = 'sw2_dhcp_snooping.txt'
    dhcp_snoop_file3 = 'sw3_dhcp_snooping.txt'
    switches_file = 'switches.yml'
    list_dhcp_snoop_files = [dhcp_snoop_file1, dhcp_snoop_file2, dhcp_snoop_file3]
    #add_data_to_dhcp_table(list_dhcp_snoop_files, db_filename)
    add_data_to_switches_table(switches_file,  db_filename)