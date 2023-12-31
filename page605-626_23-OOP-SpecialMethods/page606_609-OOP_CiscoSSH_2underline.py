# -*- coding: utf-8 -*-
# Natasha Samoilenko
# IV OOP
# 23. Специальные методы
# Подчеркивание в именах
# Два подчеркивание перед именем
# page606 -609
'''
Два подчеркивания перед именем метода используются не просто как договоренность. Такие
имена трансформируются в формат «имя класса + имя метода». Это позволяет создавать
уникальные методы и атрибуты классов.
Такое преобразование выполняется только в том случае, если в конце менее двух подчерки-
ваний или нет подчеркиваний.
'''
class Switch(object):
    __quantity = 0
    def __configure(self):
        pass
print("\nДва подчеркивание перед именем:\n", dir(Switch))
#Хотя методы создавались без приставки _Switch, она была добавлена.
#['_Switch__configure', '_Switch__quantity',

# Два подчеркивания перед и после имени
'''Таким образом обозначаются специальные переменные и методы.
Например, в модуле Python есть такие специальные переменные:
• __name__ - эта переменная равна строке __main__, когда скрипт запускается напрямую,
и равна имени модуля, когда импортируется
• __file__ - эта переменная равна имени скрипта, который был запущен напрямую, и
равна полному пути к модулю, когда он импортируется'''

import os
print('\n__ФАЙЛ v1__:\n', __file__)
print('\n__ФАЙЛ v2__:\n', os.path.abspath(__file__))

def multiply(a, b):
    return a * b
if __name__ == '__main__':
    print('\n__NAME__:\n', multiply(3, 5))