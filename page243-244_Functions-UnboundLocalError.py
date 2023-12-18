'''
Python for network engineers Natasha Samoilenko
'''
# Page range 243-
# 9 - Functions
#Ошибка UnboundLocalError: local variable referenced before assignment
#обращение к переменной в функции идет до ее создания
def f():
    print(b)
    b = 55
f()

def f():
    if 5 > 8:
        b = 55
    print(b)
f()

#обращение внутри функции к глобальной переменной, но при этом внутри функции со-
#здана такая же переменная позже
a = 10
def f():
    print(a)
    a = 55
    print(a)
f()