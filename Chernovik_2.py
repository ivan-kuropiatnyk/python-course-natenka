# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 417
# Task 17.4
import csv
import datetime

def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")

def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")

def write_last_log_to_csv(source_log, output = 'None'):
    with open(source_log, 'r') as src_log_file:
        final_list_logs = []
        read_src_log_file = csv.reader(src_log_file)
        list_src_log_file = list(read_src_log_file)
        final_list_logs.append(list_src_log_file[0])
        list_logs = list_src_log_file[1:]
        list_logs.sort(key=lambda row_inside_list: convert_str_to_datetime(row_inside_list[-1]), reverse=True)
        for list_log in list_logs:
            comparison = False
            for row_list in final_list_logs:
                if list_log[1] == row_list[1]:
                    comparison = True
            if comparison == False:
                final_list_logs.append(list_log)
    if output:
        with open(output, 'w') as dst_log_file:
            writer = csv.writer(dst_log_file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(final_list_logs)
    return final_list_logs

if __name__ == "__main__":
    print(write_last_log_to_csv('page417_mail_log.csv','page417_MY_mail_log_OUTPUT.csv' ))