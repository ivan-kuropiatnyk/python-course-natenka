'''
Python for network engineers Natasha Samoilenko
'''
# Page range 147 - 154
# try/except/else/finally
try:
    2/0
except ZeroDivisionError:
    print("You can't divide by zero")

try:
    print("Let's divide some numbers")
    2/0
    print('Cool!')
except ZeroDivisionError:
    print("You can't divide by zero")


# -*- coding: utf-8 -*-
try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print("Результат: ", int(a)/int(b))
except ValueError:
    print("Пожалуйста, вводите только числа")



# -*- coding: utf-8 -*-
try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    print("Результат: ", int(a)/int(b))
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")



#try/except/else
# -*- coding: utf-8 -*-
try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result**2)



#try/except/else
# -*- coding: utf-8 -*-
try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a)/int(b)
except (ValueError, ZeroDivisionError):
    print("Что-то пошло не так...")
else:
    print("Результат в квадрате: ", result**2)
finally:
    print("Вот и сказочке конец, а кто слушал - молодец.")


raise ValueError("При выполнении команды возникла ошибка")