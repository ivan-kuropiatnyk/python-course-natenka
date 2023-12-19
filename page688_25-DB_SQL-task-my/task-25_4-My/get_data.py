import sqlite3
import sys
from tabulate import tabulate


def get_data_by_key_value(db_name, key, value):
    keys = "mac ip vlan interface switch".split()
    if key not in keys:
        print("данный параметр не поддерживается.")
        print("допустимые значения параметров: {}".format(", ".join(keys)))
        return
    connection = sqlite3.connect(db_filename)

    query_a = "select * from dhcp where active='1' and {} = ?".format(key)
    result_a = connection.execute(query_a, (value,))
    print("\nactive записи об устройствах с такими параметрами:", key, value)
    print(tabulate(result_a))

    query_n = "select * from dhcp where active='0' and {} = ?".format(key)
    result_n = connection.execute(query_n, (value,))
    print("\nactive записи об устройствах с такими параметрами:", key, value)
    print(tabulate(result_n))

    connection.close()


def get_all_data(db_name):
    connection = sqlite3.connect(db_filename)
    print("в таблице dhcp такие active записи:")
    print(tabulate(connection.execute(" SELECT * from dhcp  WHERE active='1';")))
    print("в таблице dhcp такие non-active записи:")
    print(tabulate(connection.execute(" SELECT * from dhcp  WHERE active='0';")))
    connection.close()

def parse_args(db_name, args):
    if len(args) == 0:
        get_all_data(db_filename)
    elif len(args) == 2:
        key, value = args
        get_data_by_key_value(db_filename, key, value)
    else:
        print("пожалуйста, введите два или ноль аргументов")


if __name__ == "__main__":
    db_filename = "task_25_3_dhcp_snooping.db"
    args = sys.argv[1:]
    parse_args(db_filename, args)