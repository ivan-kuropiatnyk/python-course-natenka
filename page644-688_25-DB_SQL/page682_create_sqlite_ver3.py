# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 682
# 25
# 25.4 sqllite3 _ Пример использования SQLite
'''
Переделаем скрипт таким образом, чтобы в нём была проверка на наличие файла
dhcp_snooping.db. Если файл БД есть, то не надо создавать таблицу, считаем, что она уже
создана.
'''
import os
import sqlite3
import re

data_filename = 'page682_dhcp_snooping.txt'
db_filename = 'page682_dhcp_snooping.db'
schema_filename = 'page682_dhcp_snooping_schema.sql'

regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
result = []

with open('page682_dhcp_snooping.txt') as data:
    for line in data:
        match = regex.search(line)
        if match:
            result.append(match.groups())

db_exists = os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)

if not db_exists:
    print('Creating schema...')
    with open(schema_filename, 'r') as f:
        schema = f.read()
    conn.executescript(schema)
    print('Done')
else:
    print('Database exists, assume dhcp table does, too.')

print('Inserting DHCP Snooping data')
for row in result:
    try:
        with conn:
            query = '''insert into dhcp (mac, ip, vlan, interface)
                        values (?, ?, ?, ?)'''
            conn.execute(query, row)
    except sqlite3.IntegrityError as e:
        print('Error occured: ', e)

conn.close()