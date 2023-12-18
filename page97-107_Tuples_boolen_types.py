'''
Python for network engineers Natasha Samoilenko
'''
# Page range 97 - 107
### type data
#• Tuples (кортежи)
#Грубо говоря, кортеж - это список, который нельзя изменить. То есть, в кортеже есть только
#права на чтение. Это может быть защитой от случайных изменений.
tuple1 = tuple()
tuple2 = ('password',)
list_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
tuple_keys = tuple(list_keys)
print(tuple1, tuple2)
print(tuple_keys)
print(tuple_keys[0])
tuple_sorted = sorted(tuple_keys)
print(tuple_sorted)

#• Sets (множества)
#Множество - это изменяемый неупорядоченный тип данных. В множестве всегда содержатся
#только уникальные элементы.
vlans = [10, 20, 30, 40, 100, 10]
set_vlans = set(vlans)
print(set_vlans)
set_vlans.add(50)
print(set_vlans)
set_vlans.discard(50)
print(set_vlans)
set_vlans.clear()
print(set_vlans)

vlans1 = {10, 20, 30, 50, 100}
vlans2 = {100, 101, 102, 200}
print(vlans1 | vlans2)
print(vlans1.union(vlans2))
print(vlans1 & vlans2)
print(vlans1.intersection(vlans2))

set1 = {}
print(set1, type(set1))
set2 = set()
print(set2, type(set2))
set3 = set('long long long long string')
print(set3, type(set3))
set4 = set([10, 20, 30, 10, 10, 30])
print(set4, type(set4))

#• Boolean (логический тип данных)
items = [1, 2, 3]
empty_list = []
print(bool(items))
print(bool(empty_list))
print(bool(0))
print(bool(1))
print(bool(None))
#print(bool(a))
print("bool(items[2]) = ", bool(items[2]))

######Преобразование типов
print(int(10.007))
a = int("11111111", 2)
b = bin(10)
c = bin(255)
b2 = hex(10)
c2 = hex(255)
print("a,b,c,b2,c2 = ", a, b, c, b2, c2)
list1 = list("string")
list2 = list({1, 2, 3})
list3 = list((10, 20, 30, 40))
print("list1 =", list1)
print("list2 =", list2)
print("list3 =", list3)
set1 = set([1, 2, 3, 3, 4, 4, 4, 4])
set2 = set((1, 2, 3, 3, 4, 4, 4, 4))
set3 = set("string string")
print("set1 =", set1)
print("set2 =", set2)
print("set3 =", set3)

tuple1 = tuple([1, 2, 3, 4])
tuple2 = tuple({1, 2, 3, 4})
tuple3 = tuple("string")
print("tuple1 =", tuple1)
print("tuple2 =", tuple2)
print("tuple3 =", tuple3)

string1 = str(10)
print("string1 =", string1, type(string1))
string2 = int(string1)
print("string2 =", string2, type(string2))
print(string1.isdigit())
string3 = str('100 200 300')
print("string3.isdigit() = ", string3.isdigit())
print("string3.isalpha() = ", string3.isalpha())
print("string3.isalnum() = ", string3.isalnum())
print(type(string3) == str)
print(type(string3) == list)
print(type(string3) == tuple)

line = "switchport trunk allowed vlan 10,20,30"
words = line.split()
print("words =>", words)
vlans_split = words[-1].split(",")
print("vlans_split =", vlans_split)

line1 = "switchport trunk allowed vlan 10,20,30"
vlans1 = line1.split()[-1].split(",")
print(vlans1)