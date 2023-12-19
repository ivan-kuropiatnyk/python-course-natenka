# -*- coding: utf-8 -*-
import textfsm
traceroute = '''
r2#traceroute 90.0.0.9 source 33.0.0.2
traceroute 90.0.0.9 source 33.0.0.2
Type escape sequence to abort.
Tracing the route to 90.0.0.9
VRF info: (vrf in name/id, vrf out name/id)
  1 10.0.12.1 1 msec 0 msec 0 msec
  2 15.0.0.5  0 msec 5 msec 4 msec
  3 57.0.0.7  4 msec 1 msec 4 msec
  4 79.0.0.9  4 msec *  1 msec
'''
with open('templates/page549_traceroute.template') as template:
    fsm = textfsm.TextFSM(template)#- класс, который обрабатывает шаблон и создает из него объект в TextFSM
    result = fsm.ParseText(traceroute)#- метод, который обрабатывает переданный вывод согласно шаблону и возвращает список списков, в котором каждый элемент-это обработанная строка
print(fsm.header)#содержит имена переменных
print(result)#результат обработки