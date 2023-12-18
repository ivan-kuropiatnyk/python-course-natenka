import glob
import os
import re
import sqlite3
from pprint import pprint
import yaml

def parse_dhcp_snoop(filename):
    regex = re.compile("(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)")
    sw = re.search("(\w+)_dhcp_snooping.txt", filename).group(1)
    act1 = '1'
    with open(filename) as f:
        result = [match.groups() + (sw,) + (act1,) for match in regex.finditer(f.read())]
    return result


def add_data(db, query, data):
    connection = sqlite3.connect(db)
    for row in data:
        try:
            with connection:
                connection.execute(query, row)
        except sqlite3.IntegrityError as err:
            print("При добавлении данных:", row, "Возникла ошибка:", err)
    connection.close()

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
        if row[-2] not in list_sw:
            list_sw.append(row[-2])
            print("zeroize =>", row[-2])
            act0 = '0'
            sw = f'{row[-2]}'
            data_update = (act0, sw)
            query_update_act0 = f"UPDATE dhcp set active = ? WHERE switch = ?;"
            #cursor.execute(f"""update dhcp set active = '{act0}' where switch = '{row[-2]}';""")
            cursor.execute(query_update_act0, data_update)
    connection.commit()
    connection.close()

def add_dhcp_data(db_name, data_files):
    db_exists = os.path.exists(db_name)
    if not db_exists:
        print("База данных не существует. Перед добавлением данных, ее надо создать")
        return
    print("Добавляю данные в таблицу dhcp...")
    query = "insert or replace into dhcp values (?, ?, ?, ?, ?, ?)"
    parsed_result = []
    for filename in data_files:
        print(parse_dhcp_snoop(filename))
        parsed_result.extend(parse_dhcp_snoop(filename))
    update_data(db_name, parsed_result)
    add_data(db_name, query, parsed_result)

if __name__ == "__main__":
    db_filename = "task_25_3_dhcp_snooping.db"
    dhcp_snoop_files = glob.glob("./new_data/sw*_dhcp_snooping.txt")
    add_dhcp_data(db_filename, dhcp_snoop_files)