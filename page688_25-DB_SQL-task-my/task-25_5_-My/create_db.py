# -*- coding: utf-8 -*-
import os
import sqlite3

def verify_file_exist(filename):
    filename_verified = os.path.exists(filename)
    return filename_verified

def create_db(db_file, schema_file):
    db_file_exist = verify_file_exist(db_file)
    schema_file_exist = verify_file_exist(schema_file)
    if not db_file_exist:
        print('Database was not found, trying to create a new one')
        if schema_file_exist:
            print('Creating DB using SQL schema...')
            with open(schema_filename, 'r') as f:
                schema = f.read()
            conn = sqlite3.connect(db_filename)
            conn.executescript(schema)
            conn.close()
            print('Done')
        else:
            print(f'Can not find file {schema_file}')
            print('To move further could you kindly to create a schema at first')
    else:
        print('Database exists, you can start to use add_data to fill Database')

if __name__ == '__main__':
    db_filename = 'task_25_5_dhcp_snooping.db'
    schema_filename = 'dhcp_snooping_schema.sql'
    create_db(db_filename, schema_filename)