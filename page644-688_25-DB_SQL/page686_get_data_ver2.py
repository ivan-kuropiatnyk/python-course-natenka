# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 684
# 25
# 25.4 sqllite3 _ Пример использования SQLite
'''
Вторая версия скрипта для получения данных с небольшими улучшениями:
• Вместо форматирования строк используется словарь, в котором описаны запросы, соот-
ветствующие каждому ключу.
• Выполняется проверка ключа, который был выбран
• Для получения заголовков всех столбцов, который соответствуют запросу, используется
метод keys()
'''
import sqlite3
import sys
db_filename = 'page682_dhcp_snooping.db'
query_dict = {
'vlan': 'select mac, ip, interface from dhcp where vlan = ?',
'mac': 'select vlan, ip, interface from dhcp where mac = ?',
'ip': 'select vlan, mac, interface from dhcp where ip = ?',
'interface': 'select vlan, mac, ip from dhcp where interface = ?'
}
key, value = sys.argv[1:]
keys = query_dict.keys()
if not key in keys:
    print('Enter key from {}'.format(', '.join(keys)))
else:
    conn = sqlite3.connect(db_filename)

    conn.row_factory = sqlite3.Row

    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)

    query = query_dict[key]
    result = conn.execute(query, (value, ))
    for row in result:
        for row_name in row.keys():
            print('{:12}: {}'.format(row_name, row[row_name]))
        print('-' * 40)
'''
ivankurop@vb-ub22:~/PycharmProjects/pythonProjectNata1/page644-_25-DB_SQL-$ python3 page686_get_data_ver2.py vlan 10  

Detailed information for host(s) with vlan 10
----------------------------------------
mac         : 00:09:BB:3D:D6:58
ip          : 10.1.10.2
interface   : FastEthernet0/1
----------------------------------------
mac         : 00:09:BC:3F:A6:50
ip          : 10.1.10.6
interface   : FastEthernet0/3
----------------------------------------
ivankurop@vb-ub22:~/PycharmProjects/pythonProjectNata1/page644-_25-DB_SQL-$ python3 page686_get_data_ver2.py ip
Traceback (most recent call last):
  File "/home/ivankurop/PycharmProjects/pythonProjectNata1/page644-_25-DB_SQL-/page686_get_data_ver2.py", line 25, in <module>
    key, value = sys.argv[1:]
ValueError: not enough values to unpack (expected 2, got 1)
'''