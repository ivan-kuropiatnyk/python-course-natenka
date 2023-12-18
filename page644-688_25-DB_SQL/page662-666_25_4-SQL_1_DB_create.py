# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 662-666
# 25
# 25.4 sqllite3 _ Creation DB
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

# Для выполнения команд SQL в модуле есть несколько методов:
###• execute - метод для выполнения одного выражения SQL
###• executemany - метод позволяет выполнить одно выражение SQL для последовательности параметров (или для итератора)
###• executescript - метод позволяет выполнить несколько выражений SQL за один раз

###     • execute
print("______________25.4_1_EXECUTE_______________________\n")

connection_execute = sqlite3.connect('dhcp_snooping_pages662-666.db')  # -подключение к конкретной БД
cursor_execute = connection_execute.cursor()  # объект Cursor - это основной способ работы с БД.

cursor_execute.execute("create table switch (mac text not NULL primary key, hostname text, model text, location text)")
data_execute = [
    ('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
    ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
    ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
    ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]

# таблицу switch нужно заполнить данными из списка data Для этого можно использовать запрос вида:
query = "INSERT into switch values (?, ?, ?, ?)"
for row in data_execute:
    cursor_execute.execute(query, row)
connection_execute.commit()

###     • executemany
print("\n______________25.4_2_EXECUTEMANY_______________________\n")
data_executemany = [
    ('0000.1111.0001', 'sw5', 'Cisco 3750', 'London, Green Str'),
    ('0000.1111.0002', 'sw6', 'Cisco 3750', 'London, Green Str'),
    ('0000.1111.0003', 'sw7', 'Cisco 3750', 'London, Green Str'),
    ('0000.1111.0004', 'sw8', 'Cisco 3750', 'London, Green Str')]
connection_executemany = sqlite3.connect('dhcp_snooping_pages662-666.db')
cursor_executemany = connection_executemany.cursor()

query_executemany = "INSERT into switch values (?, ?, ?, ?)"

cursor_executemany.executemany(query_executemany, data_executemany)
connection_executemany.commit()

###• executescript
print("\n______________25.4_2_EXECUTESCRIPT_______________________\n")
connection_executescript = sqlite3.connect('dhcp_snooping_pages662-666.db')
cursor_executescript = connection_executescript.cursor()
cursor_executescript.executescript('''
	create table switches(
	hostname text not NULL primary key,
	location text
	);

	create table dhcp(
		mac text not NULL primary key,
		ip text,
		vlan text,
		interface text,
		switch text not null references switches(hostname)
	);
''')

