# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 675
# 25
# 25.4 sqllite3 _ Connection как менеджер контекста
#
# Python позволяет использовать объект Connection как менеджер контекста. В таком случае
# не нужно явно делать commit.
# При этом:
# • при возникновении исключения, транзакция автоматически откатывается
# • если исключения не было, автоматически выполняется commit
from pprint import pprint
import sqlite3
import page673_create_sw_inventory_ver2_functions as dbf
#MAC-адрес sw7 совпадает с MAC-адресом коммутатора sw3 в списке data
data2 = [('0055.AAAA.CCCC', 'sw5', 'Cisco 3750', 'London, Green Str'),
        ('0066.BBBB.CCCC', 'sw6', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw7', 'Cisco 2960', 'London, Green Str'),
        ('0088.AAAA.CCCC', 'sw8', 'Cisco 3750', 'London, Green Str')]
con = dbf.create_connection('sw_inventory3.db')
query_insert = "INSERT into switch values (?, ?, ?, ?)"
query_get_all = "SELECT * from switch"
print("\nПроверка текущего содержимого БД")
pprint(dbf.get_all_from_db(con, query_get_all))
print('-' * 60)
print("Попытка записать данные с повторяющимся MAC-адресом:")
pprint(data2)
dbf.write_data_to_db(con, query_insert, data2)
print("\nПроверка содержимого БД")
pprint(dbf.get_all_from_db(con, query_get_all))
con.close()