# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 684
# 25
# 25.4 sqllite3 _ Пример использования SQLite
'''
скрипт, который занимается отправкой запросов в БД и выводом
результатов. Он должен:
• ожидать от пользователя ввода параметров:
– имя параметра
– значение параметра
• делать нормальный вывод данных по запросу

Комментарии к скрипту:
• из аргументов, которые передали скрипту, считываются параметры key, value
– из списка keys удаляется выбранный ключ. Таким образом, в списке остаются только
те параметры, которые нужно вывести
• подключаемся к БД
– conn.row_factory = sqlite3.Row - позволяет далее обращаться к данным в колон-
ках по имени колонки
• из БД выбираются те строки, в которых ключ равен указанному значению
– в SQL значения можно подставлять через знак вопроса, но нельзя подставлять имя
столбца. Поэтому имя столбца подставляется через форматирование строк, а зна-
чение - штатным средством SQL.
– Обратите внимание на (value,) - таким образом передается кортеж с одним эле-
ментом
• Полученная информация выводится на стандартный поток вывода: * перебираем полу-
ченные результаты и выводим только те поля, названия
которых находятся в списке keys
'''
import sqlite3
import sys

db_filename = 'page682_dhcp_snooping.db'
key, value = sys.argv[1:]
keys = ['mac', 'ip', 'vlan', 'interface']

keys.remove(key)

conn = sqlite3.connect(db_filename)

#Позволяет далее обращаться к данным в колонках, по имени колонки
conn.row_factory = sqlite3.Row

print('\nDetailed information for host(s) with', key, value)
print('-' * 40)

query = 'select * from dhcp where {} = ?'.format(key)
result = conn.execute(query, (value, ))

for row in result:
    for k in keys:
        print('{:12}: {}'.format(k, row[k]))
    print('-' * 40)
'''
ivankurop@vb-ub22:~/PycharmProjects/pythonProjectNata1/page644-_25-DB_SQL-$ python3 page684_get_data_ver1.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
----------------------------------------

ivankurop@vb-ub22:~/PycharmProjects/pythonProjectNata1/page644-_25-DB_SQL-$ python3 page684_get_data_ver1.py vlan 10

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
'''