'''
Python for network engineers Natasha Samoilenko
'''
# Page from 63-67

### Variables
##### Page 63
a = 3
b = 'Hello'
c = "HELLO"
d, e = 9, 'test'
print(a, b, c, d, e)
a=b=c=33
id(a)#показывает идентификатор объекта
print('id(a) =',id(a))
print('id(b) =',id(b))
print('id(c) =',id(c))
print(a, b, c,)
'''
числа от -5 до
256 заранее созданы и хранятся в массиве (списке). Поэтому при создании числа из этого
диапазона фактически создаётся ссылка на число в созданном массиве.
При этом, если сделать присваивание переменных друг другу, то идентификаторы будут у
всех одинаковые
'''