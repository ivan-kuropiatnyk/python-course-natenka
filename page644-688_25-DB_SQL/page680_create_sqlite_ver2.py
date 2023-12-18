# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 680
# 25
# 25.4 sqllite3 _ Пример использования SQLite
'''
Комментарии к скрипту:
• в регулярном выражении, которое проходится по выводу команды sh ip dhcp snooping
binding, используются не именованные группы, как в примере раздела Регулярные вы-
ражения, а нумерованные
– группы созданы только для тех элементов, которые нас интересуют
• result - это список, в котором хранится результат обработки вывода команды
– но теперь тут не словари, а кортежи с результатами
– это нужно для того, чтобы их можно было сразу передавать на запись в БД
• Перебираем в полученном списке кортежей элементы
• В этом скрипте используется еще один вариант записи в БД
– строка query описывает запрос. Но вместо значений указываются знаки вопроса.
Такой вариант записи запроса позволяет динамически подставлять значение полей
– затем методу execute передается строка запроса и кортеж row, где находятся зна-
чения
'''
import sqlite3
import re

regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
result = []

with open('page680_dhcp_snooping.txt') as data:
    for line in data:
        match = regex.search(line)
        if match:
            result.append(match.groups())

conn = sqlite3.connect('page680_dhcp_snooping.db')
print('Creating schema...')

with open('page680_dhcp_snooping_schema.sql', 'r') as f:
    schema = f.read()
    conn.executescript(schema)

print('Done')
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