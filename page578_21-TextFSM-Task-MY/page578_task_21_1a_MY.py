# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM.
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt
и шаблоне templates/sh_ip_int_br.template.
"""
from pprint import pprint
import textfsm

def parse_output_to_dict(template, command_output):
    with open(template) as templ:
        result = []
        fsm = textfsm.TextFSM(templ)  # - класс, который обрабатывает шаблон и создает из него объект в TextFSM
        header = fsm.header
        parsed = fsm.ParseText(command_output)
        #result = [dict(zip(header, raw)) for raw in parsed]
        for raw in parsed:
            result.append(dict(zip(header, raw)))
    return result

if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as show:
        output = show.read()
    result = parse_output_to_dict("templates/sh_ip_int_br.template.txt", output)
    pprint(result, width=100)