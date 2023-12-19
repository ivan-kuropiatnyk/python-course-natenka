# -*- coding: utf-8 -*-
import sqlite3
import sys

def connect_to_db(*args, db_filename='task_25_2_dhcp_snooping.db'):
#key, value - is possible to give in a positional or kwargs arguments but db_filename= - just as kwargs
# Script will show just a print "Cкрипт поддерживает... in the case if in the script
# beside key,value and db_filename, will be some another arguments in *args
    args = args[0]
    conn = sqlite3.connect(db_filename)
    # Позволяет далее обращаться к данным в колонках, по имени колонки
    conn.row_factory = sqlite3.Row
    if len(args) == 0:
        print("два аргументa")
        query = 'select * from dhcp;'
        result = conn.execute(query)
    elif len(args) == 2:
        query = 'select * from dhcp where {} = ?'.format(args[0])
        result = conn.execute(query, (args[1],))
    else:
        print("Cкрипт поддерживает только два или ноль аргументов ")
        return
    return key_value_parse(result, key_parser=None, value_parser=None)

def key_value_parse(result, key_parser=None, value_parser=None):
    key = key_parser
    value = value_parser
    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    if key:
        keys.remove(key)
    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)
    for row in result:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)

if __name__ == "__main__":
    db_filename = 'task_25_2_dhcp_snooping.db'
    #connect_to_db(key='vlan', value='10')
    #connect_to_db(key='ip')
    connect_to_db(sys.argv[1:])