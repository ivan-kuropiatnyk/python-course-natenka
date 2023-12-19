# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 679
# 25
# 25.4 sqllite3 _ Пример использования SQLite
'''
Комментарии к файлу:
• при выполнении строки conn = sqlite3.connect('dhcp_snooping.db'):
– создается файл dhcp_snooping.db, если его нет
– создается объект Connection
• в БД создается таблица (если ее не было) на основании команд, которые указаны в фай-
ле dhcp_snooping_schema.sql:
– открывается файл dhcp_snooping_schema.sql
– schema = f.read() - весь файл считывается в одну строку
– conn.executescript(schema) - метод executescript позволяет выполнять команды
SQL, которые прописаны в файле
'''
import sqlite3
conn = sqlite3.connect('page679_dhcp_snooping.db')
print('Creating schema...')
with open('page679_dhcp_snooping_schema.sql', 'r') as f:
    schema = f.read()
    conn.executescript(schema)
print("Done")
conn.close()