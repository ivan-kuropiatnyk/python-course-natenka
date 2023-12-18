# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 417
# Task 17.2
"""
• взять содержимое нескольких файлов с выводом команды sh version
• получить информацию об устройстве
• записать полученную информацию в файл в CSV формате

Функция parse_sh_version:
• ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
• возвращает кортеж из трёх элементов:
– ios - в формате «12.4(5)T»
– image - в формате «flash:c2800-advipservicesk9-mz.124-5.T.bin»
– uptime - в формате «5 days, 3 hours, 3 minutes»

У функции write_inventory_to_csv должно быть два параметра:
• data_filenames - список имен файлов с выводом sh version
• csv_filename - имя файла (например, routers_inventory.csv)
Функция write_inventory_to_csv записывает содержимое в файл, в формате CSV и ничего не
возвращает
Функция write_inventory_to_csv должна делать следующее:
• обработать информацию из каждого файла с выводом sh version:
– sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
• с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
• из имени файла нужно получить имя хоста
• после этого вся информация должна быть записана в CSV файл
В файле routers_inventory.csv должны быть такие столбцы: 
hostname, ios, image, uptime
В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое
списка.
Кроме того, создан список заголовков (headers), который должен быть записан в CSV.

"""
import csv
import re
import glob


def parse_sh_version(sh_version):
    #print(sh_version)
    regex_ios_uptime_image = (r'^\S+ IOS Software, (?P<ios>\S+).*(?:\\n|\n)'
                              r'.*'
                              r'router uptime is (?P<uptime>[\w,\s]+).*(?:\\n|\n)'
                              r'.*'
                              r'System image file is "\S+:(?P<image>.+T\w*).*"(?:\\n|\n)'
                              )
    match_ios_uptime_image = re.findall(regex_ios_uptime_image, sh_version)
    return match_ios_uptime_image[0]
def write_inventory_to_csv(data_filenames, to_file_csv):
    headers = ["hostname", "ios", "image", "uptime"]
    list_all = []
    list_all.append(headers)
    for filename in data_filenames:#перебираем файлы
        regex_hostname = r'\S+_(?P<hostname>\S+).txt'
        match_hostname = re.search(regex_hostname, filename)
        hostname = match_hostname.group('hostname')
        with open(filename, 'r') as src, open(to_file_csv, 'w') as dst:
            output_show_version = str(src.readlines())
            ios, uptime, image = parse_sh_version(output_show_version)#вызов функции вверху
            list_local = [hostname, ios, uptime, image]
            list_all.append(list_local)
            writer = csv.writer(dst)
            writer.writerows(list_all)
if __name__ == '__main__':
    sh_version_files = glob.glob("page417_sh_vers*.txt")
    write_inventory_to_csv(sh_version_files, 'page417_shver.csv')