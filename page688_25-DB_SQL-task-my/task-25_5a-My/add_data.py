import glob
import os
import re
import sqlite3
#import time # 1st and 2nd variant
from datetime import datetime # 3rd variant
from pprint import pprint
import yaml
from tabulate import tabulate

def add_data(db, query, data):
    connection = sqlite3.connect(db)
    for row in data:
        try:
            with connection:
                connection.execute(query, row)
        except sqlite3.IntegrityError as err:
            print("При добавлении данных:", row, "Возникла ошибка:", err)
    connection.close()

def add_dhcp_data(db_name, data_files):
    db_exists = os.path.exists(db_name)
    if not db_exists:
        print("База данных не существует. Перед добавлением данных, ее надо создать")
        return
    print("Добавляю данные в таблицу dhcp...")
    query = "insert or replace into dhcp values (?, ?, ?, ?, ?, ?, ?)"
    parsed_result = []
    for filename in data_files:
        print(parse_dhcp_snoop(filename))
        parsed_result.extend(parse_dhcp_snoop(filename))
    update_data(db_name, parsed_result)
    add_data(db_name, query, parsed_result)
    del_non_act(db_name)

def del_non_act(db_filename):
    '''
    this function deletes values in dhcp table in db where active = 0 and last time updated is more than 7days
    '''
    connection = sqlite3.connect(db_filename)
    query_0 = "select time_con from dhcp where active='0'"
    result_0 = connection.execute(query_0)
    for time_con in result_0:
        time_con = str(time_con).replace('(','').replace(')','').replace('\'','').replace('\"','').replace(',','')
        #print("SUCH TIME WITH NON-ACTIVE =>", time_con)
        datetime_old = datetime.strptime(time_con, "%Y-%m-%d %H:%M:%S")
        datetime_current = datetime.now()
        datetime_difference = datetime_current.timestamp() - datetime_old.timestamp()
        if datetime_difference >= 604800:#7days = 604800sec
            #the values with _info exists just for show which data will be deleted
            query_info = f"select * from dhcp where time_con = '{time_con}';"
            result_info = connection.execute(query_info)
            for del_info in result_info:
                print("The next data will be deleted=>\n", del_info)
            query_del = f"DELETE from dhcp WHERE time_con = '{time_con}';"#time_con - because it is in text somehow with datetime_old it had not worked
            connection.execute(query_del)
    connection.commit()
    connection.close()

def parse_dhcp_snoop(filename):
    regex = re.compile("(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)")
    sw = re.search("(\w+)_dhcp_snooping.txt", filename).group(1)
    act1 = '1'
    local_time = datetime.now()#3rd variant
    #local_time = time.localtime()#1st and 2nd variant
    # YYYY-MM-DD HH:MM:SS
    #con_time = f"{local_time.tm_year}-{local_time.tm_mon}-{local_time.tm_mday} {local_time.tm_hour}:{local_time.tm_min}:{local_time.tm_sec}" #1st variant
    #con_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)#2nd variant
    con_time = datetime.strftime(local_time, "%Y-%m-%d %H:%M:%S")#3rd variant
    with open(filename) as f:
        result = [match.groups() + (sw,) + (act1,) + (con_time,) for match in regex.finditer(f.read())]
    return result

def update_data(db, parsed_result):
    '''
    Function takes parsed result(after function parse_dhcp_snoop(filename)) what will be
    further added to databased by the function add_data(db, query, data), so the goal of this
    function is to zeroize the column "active" in the database for switches where the data will
    be added. Zeroizing means to add 0 to this column as marking this mac as non-actvie.
    '''
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    list_sw = []
    for row in parsed_result:
        sw = f'{row[-3]}'
        if sw not in list_sw:
            list_sw.append(sw)
            print("zeroize =>", sw)
            act0 = '0'
            #sw = f'{row[-2]}'
            data_update = (act0, sw)
            query_update_act0 = f"UPDATE dhcp set active = ? WHERE switch = ?;"
            #cursor.execute(f"""update dhcp set active = '{act0}' where switch = '{row[-2]}';""")
            cursor.execute(query_update_act0, data_update)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_filename = "task_25_5a_dhcp_snooping.db"
    dhcp_snoop_files = glob.glob("./new_data/sw*_dhcp_snooping.txt")
    add_dhcp_data(db_filename, dhcp_snoop_files)