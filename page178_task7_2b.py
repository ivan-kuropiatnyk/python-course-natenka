'''
Python for network engineers Natasha Samoilenko
'''
# Page range 178
# TASK 7.2b
#Запуск как ниже в строке-примере:
#D:\Literature\Python\PyMyProgNatenka1> python.exe page178_task7_2.py config_sw1.txt
from sys import argv
ignore = ["duplex", "alias", "configuration"]
file_read = open('config_sw1.txt',mode='r',encoding='latin_1')
file_write = open('task_7.2b_result.txt', 'w', encoding='latin_1')
file_read.readline()
lines_as_string = ""

for line in file_read:

    if "!" not in line:

        if ignore[0] in line:
            pass
        elif ignore[1] in line:
            pass
        elif ignore[2] in line:
            pass
        else:
            line = line.rstrip()+"\n"
            lines_as_string = lines_as_string + line

print(lines_as_string)
file_write.write(lines_as_string)

file_write.close()
file_read.close()