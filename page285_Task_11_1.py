# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 285
# Task 11.1
def parse_cdp_neighbors(command_output):#command_output as <class 'str'>
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде
    будет получен вывод команды с оборудования. Принимая как аргумент вывод
    команды, вместо имени файла, мы делаем функцию более универсальной: она может
    работать и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    Функция обрабатывает вывод show cdp neighbors и выдает словарь где ключ текущего
    устройства =hostname + исходящий ифейс, значение удаленного устройства=hostname+
    входящий ифейс
    """
    command_output_split = command_output.split("\n")#as <class 'list'>
    hostname = ''
    dict_all = {}
    j = 0
    for line in command_output_split:
        new_line = []
        if len(line) > 0 and '>' in line and j == 0:
            hostname = line[:line.index('>')]
            new_line.append(line[:line.index('>')])
        elif "Device ID" in line:
            j += 1
        elif len(line) > 0 and j > 0:
            line = list(line.split(" "))
            line = [i for i in line if len(i) > 2 and i.isdigit() == False or 'R' in i]
            line = list(filter(lambda x: len(x) > 1, line))
            new_line.append(hostname)
            new_line.append(f'{line[1]+line[2]}')
            new_line.append(line[0])
            new_line.append(f'{line[-2] + line[-1]}')
            tuple_key = tuple(new_line[:2])
            tuple_value = tuple(new_line[2:])
            dict_all[tuple_key] = tuple_value
    return dict_all
if __name__ == "__main__":
    #считывает все содержимое файла в строку, а затем передать строку как аргумент функции:
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))