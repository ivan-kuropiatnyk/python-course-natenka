'''
Python for network engineers Natasha Samoilenko
'''
# Page range 67-70

### type data
##### Page 67
#• Numbers (числа)
a = 1+2
b = 2.0-1
c = 2*3
d = 2**3
##Деление int и float:
e = 10/3
print("a = {}, b = {}, c = {}, d = {}, e = {}".format(a,b,c,d,e))
##С помощью функции round можно округлять числа до нужного количества знаков:
rounded_3x = round(e, 3)
rounded_4x = round(e, 4)
print("rounded_3x =",rounded_3x)
print("rounded_4x =",rounded_4x)
##Остаток от деления
ost_deleniya = 10 % 3
print("ost_deleniya =",ost_deleniya)
##Операторы сравнения
print("10 > 3.0 it is ",10 > 3.0)
print("10 == 3 it is ",10 == 3)
print("10 == 10 it is ",10 == 10)
print("10 != 3 it is ",10 != 3)
print("10 >= 7 it is ",10 >= 7)
print("10 =< 7 it is ",10 <= 7)
### Convert integer to string
str_a = '10'
print("string a => ", str_a, str_a+str_a)
num_a = int(str_a)
print("a converted to number => ",num_a ,num_a+num_a)
###Если указать, что строку a надо воспринимать как двоичное число, то результат будет таким:
num_aa = int(str_a, 2)
print("a converted двоичное число => ",num_aa ,num_aa+num_aa)
float_a = float(str_a)
float_aa = format((round(float_a)), ".3f")
print("a converted float =>", float_a)
print("a converted with decimal points =>", float_aa)
###двоичное представление числа
binary_a = bin(num_a)
print("a converted to binary =>", binary_a)
### 16 hexadecimal number
hex_a = hex(num_a)
print("a converted to hexadecimal =>", hex_a)
import math
print("math.sqrt(9)=",math.sqrt(9))
print("math.sqrt(10)=",math.sqrt(10))
print("math.factorial(3)=",math.factorial(3))
print("math.pi =",math.pi)

#• Strings (строки)
#• Lists (списки)
#• Dictionaries (словари)
#• Tuples (кортежи)
#• Sets (множества)
#• Boolean (логический тип данных)
#Эти типы данных можно, в свою очередь, классифицировать по нескольким признакам:
#• изменяемые (списки, словари и множества)
#• неизменяемые (числа, строки и кортежи)
#• упорядоченные (списки, кортежи, строки и словари)
#• неупорядоченные (множества)