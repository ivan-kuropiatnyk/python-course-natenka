'''
Python for network engineers Natasha Samoilenko
'''
# Page range 178
# TASK 7.3
"""
CAM_table.txt. Каждая строка, где есть MAC-адрес, должна быть обработана 
таким образом, чтобы на стандартный поток вывода была выведена таблица вида:
100 01bb.c580.7000 Gi0/1
"""
with open('CAM_table.txt', 'r', encoding='latin_1') as src:
    i = 0
    lines_as_string = ""
    for line in src:
        if 'DYNAMIC' in line:
            line = line.rstrip() + "\n"
            line_list = line.split()
            mac_index = line_list[1].replace(".","")
            if len(mac_index) == 12:
                lines_as_string = lines_as_string + line
print(lines_as_string)