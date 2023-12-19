# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 672
# 25
# 25.4 sqllite3 _ Connection как менеджер контекста
#
# Python позволяет использовать объект Connection как менеджер контекста. В таком случае
# не нужно явно делать commit.
# При этом:
# • при возникновении исключения, транзакция автоматически откатывается
# • если исключения не было, автоматически выполняется commit

import sqlite3

data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]
con = sqlite3.connect('page672_sw_inventory3.db')
con.execute('''create table switch
(mac text not NULL primary key, hostname text, model text, location text)'''
            )
try:
    with con:
        query = 'INSERT into switch values (?, ?, ?, ?)'
        con.executemany(query, data)
except sqlite3.IntegrityError as e:
    print('Возникла ошибка: ', e)

for row in con.execute('select * from switch'):
    print(row)
con.close()
