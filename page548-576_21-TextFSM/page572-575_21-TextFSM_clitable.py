# -*- coding: utf-8 -*-
#page573 - Для начала импортируем класс clitable
from textfsm import clitable
#page573 - Считываем вывод, который хранится в файле output/sh_ip_route_ospf.txt, в строку:
with open('output/sh_ip_route_ospf.txt') as f:
    output_sh_ip_route_ospf = f.read()
    print(
        "Считываем вывод файла sh_ip_route_ospf.txt в одну строку =>\n",
          output_sh_ip_route_ospf
          )

#Сначала надо инициализировать класс, передав ему имя файла, в котором хранится соответ-
#ствие между шаблонами и командами, и указать имя каталога, в котором хранятся шаблоны:
cli_table = clitable.CliTable('index', 'templates')
print("cli_table =>\n", cli_table)

#Надо указать, какая команда передается, и указать дополнительные атрибуты, которые по-
#могут идентифицировать шаблон. Для этого нужно создать словарь, в котором ключи - имена
#столбцов, которые определены в файле index.
attributes = {'Command': 'show ip route ospf', 'Vendor': 'cisco_ios'}
print("attributes =>\n", attributes)

#Методу ParseCmd надо передать вывод команды и словарь с параметрами:
print(cli_table.ParseCmd(output_sh_ip_route_ospf, attributes))
print("\ncli_table =>\n", cli_table)

#В результате в объекте cli_table получаем обработанный вывод команды sh ip route ospf.

#Методы cli_table (чтобы посмотреть все методы
print("Методы cli_table =>\n", dir(cli_table))

#Метод FormattedTable позволяет получить вывод в виде таблицы:
formatted_table = cli_table.FormattedTable()
print("\nformatted table =>\n", formatted_table)

#Чтобы получить из объекта cli_table структурированный вывод, например, список списков,
#надо обратиться к объекту таким образом:
data_rows = [list(row) for row in cli_table]
print("data_rows =>\n", data_rows)