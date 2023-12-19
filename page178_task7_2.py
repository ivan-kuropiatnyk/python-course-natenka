'''
Python for network engineers Natasha Samoilenko
'''
# Page range 178
# TASK 7.2
#Запуск как ниже в строке-примере:
#D:\Literature\Python\PyMyProgNatenka1> python.exe page178_task7_2.py config_sw1.txt
from sys import argv
file_read = open('config_sw1.txt',mode='r',encoding='latin_1')
file_read.readline()
for line in file_read:
    if "!" not in line:
        print (line.rstrip())
file_read.close()