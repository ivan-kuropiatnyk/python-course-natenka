# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 670
# 25
# 25.4 sqllite3 Использование модуля sqlite3 без явного создания курсора
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

data = [('0000.AAAA.CCCC', 'sw1', 'Cisco 3750', 'London, Green Str'),
        ('0000.BBBB.CCCC', 'sw2', 'Cisco 3780', 'London, Green Str'),
        ('0000.AAAA.DDDD', 'sw3', 'Cisco 2960', 'London, Green Str'),
        ('0011.AAAA.CCCC', 'sw4', 'Cisco 3750', 'London, Green Str')]

con = sqlite3.connect('sw_inventory2.db')
con.execute('''create table switch
            (mac text not NULL primary key, hostname text, model text, location text)'''
            )

query = 'INSERT into switch values (?, ?, ?, ?)'

con.executemany(query, data)
con.commit()
for row in con.execute('select * from switch'):
    print(row)
con.close()
