# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 666-670
# 25
# 25.4 sqllite3 _ show DB
'''
litecli new_db.db

create table switch (mac text not NULL primary key, hostname text, model text, location text)

DROP table switch;

source add_rows_to_testdb.txt
source update_fields_in_testdb.txt

ALTER table switch ADD COLUMN mngmt_ip text;

UPDATE switch set mngmt_ip = '10.255.1.2', mngmt_vid = 255 WHERE hostname = 'sw2';
UPDATE switch set model = 'Cisco 3850', mac = '0010.D1DD.E1EE' WHERE hostname = 'sw1';

INSERT into switch values ('0010.A1AA.C1CC', 'sw1', 'Cisco 3750', 'London, Green Str');
INSERT into switch (mac, model, location, hostname) values ('0020.A2AA.C2CC', 'Cisco 3850', 'London, Green Str', 'sw2');
INSERT INTO switch VALUES ('0030.A3AA.C1CC', 'sw3', 'Cisco 3850', 'London, Green Str', '10.255.1.3', 255);
INSERT OR REPLACE INTO switch VALUES ('0030.A3AA.C1CC', 'sw3', 'Cisco 3850', 'London, Green Str', '10.255.1.3', 255);

REPLACE INTO switch VALUES ('0030.A3AA.C1CC', 'sw3', 'Cisco 3850', 'London, Green Str', '10.255.1.3', 255);
REPLACE INTO switch VALUES ('0080.A8AA.C8CC', 'sw8', 'Cisco 3850', 'London, Green Str', '10.255.1.8', 255);

DELETE from switch where hostname = 'sw8';

SELECT * from switch;
SELECT hostname, mac, model from switch;
SELECT * from switch ORDER BY hostname ASC;
SELECT * from switch ORDER BY mngmt_ip DESC;
SELECT * from switch WHERE model = 'Cisco 3750';
SELECT * from switch WHERE model LIKE '%3750';
###  _ - обозначает один символ или число
###  % - обозначает ноль, один или много символов
select * from switch where model = 'Cisco 3850' and mngmt_ip LIKE '10.255.%';
select * from switch where model in ('Cisco 3750', 'C3750');
select * from switch where model not in ('Cisco 3750', 'C3750');
select * from switch where model LIKE '%3750' or model LIKE '%3850';
'''
import sqlite3

# Получение результатов запроса
# Для получения результатов запроса в sqlite3 есть несколько способов:
### • использование методов fetch - в зависимости от метода возвращаются одна, несколько или все строки
### • использование курсора как итератора - возвращается итератор

# Метод fetchone
print("\n__________FETCHONE___________\n")
# Метод fetchone возвращает одну строку данных.
connection_fetchone = sqlite3.connect('new_db.db')
cursor_fetchone = connection_fetchone.cursor()
cursor_fetchone.execute('select * from switch')
print("First string = ", cursor_fetchone.fetchone())
print("Second string = ", cursor_fetchone.fetchone())

#После обработки всех
#строк метод начинает возвращать None.
#За счет этого метод можно использовать в цикле, например, так:
cursor_fetchone.execute('select * from switch')
i = 0
while True:
    next_row_fetchone = cursor_fetchone.fetchone()
    i += 1
    if next_row_fetchone:
        print(f"DB by cycle, string{i} => ", next_row_fetchone)
    else:
        print(f"DB by cycle, string{i} => ", next_row_fetchone, "=> It is the END of the DB and here you are seeing None")
        break

print("\n__________FETCHMANY___________\n")
#Метод fetchmany возвращает список строк данных.
#Синтаксис метода:
#cursor.fetchmany([size=cursor.arraysize])
#С помощью параметра size можно указывать, какое количество строк возвращается. По умол-
#чанию параметр size равен значению cursor.arraysize:
connection_fetchmany = sqlite3.connect('new_db.db')
cursor_fetchmany = connection_fetchone.cursor()
cursor_fetchmany.execute('select * from switch')
print('Quantity of string to return => ', cursor_fetchmany.arraysize)
cursor_fetchmany.execute('select * from switch')
#Метод выдает нужное количество строк, а если строк осталось меньше, чем параметр size,
#то оставшиеся строки.
from pprint import pprint
j = 0
while True:
    three_rows_fetchmany = cursor_fetchmany.fetchmany(3)#по три строки из запроса
    if three_rows_fetchmany:
        j += 3
        print(f"strings{j-2}-{j}=> ", three_rows_fetchmany)
    else:
        break

print("\n__________FETCHALL___________\n")
#Метод fetchall - возвращает все строки в виде списка:
connection_fetchall = sqlite3.connect('new_db.db')
cursor_fetchall = connection_fetchone.cursor()
cursor_fetchall.execute('select * from switch')
list_fetchall = cursor_fetchall.fetchall()
k = 0
for string in list_fetchall:
    k += 1
    print(f"FETCHALL string{k}=> ",string)
#Важный аспект работы метода - он возвращает все оставшиеся строки.
#То есть, если до метода fetchall использовался, например, метод fetchone, то метод fetchall
#вернет оставшиеся строки запроса
cursor_fetchall.execute('select * from switch')
cursor_fetchall.fetchmany(6)
print(f"after fetchmany(6) FETCHALL =>", cursor_fetchall.fetchall())


print("\n__________CURSOR AS ITERATOR___________\n")
#Cursor как итератор
#Если нужно построчно обрабатывать результирующие строки, лучше использовать курсор
#как итератор. При этом не нужно использовать методы fetch.
connection_cursor_iterator = sqlite3.connect('new_db.db')
cursor_cursor_iterator = connection_fetchone.cursor()
result_cursor_iterator = cursor_cursor_iterator.execute('select * from switch')
l = 0
for row in result_cursor_iterator:
    l += 1
    print(f"CURSOR string{l}=>", row)
# or another variant:
l = 0
for row in cursor_cursor_iterator.execute('select * from switch'):
    l += 1
    print(f"_CURSOR_2 string{l}=>", row)