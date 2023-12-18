'''
Python for network engineers Natasha Samoilenko
'''
# Page range 83 - 87
### type data
##### Page 83
#• Lists (списки)
list1 = [10,20,30,77]
list2 = ['one', 'dog', 'seven']
list3 = [1, 20, 4.0, 'word']
vlans = ['10', '15', '20', '30', '100-200']
print("list1 = ", list1)
print("list2 = ", list2)
print("list3 = ", list3)
print("vlans = ", vlans)
list4 = list('router')
print("list4 = ", list4)
vlans_R = vlans
vlans_R.reverse()
print("vlans_R = ", vlans_R)
list3[-1] = 'test'
print("list3 with test = ", list3)
interfaces = [
['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]
print(interfaces)
names = ['John', 'Michael', 'Antony']
print(sorted(names))

vlans.append('300')
print("vlans.append('300')=", vlans)

vlans2 = ['300', '400', '500']
vlans_E = vlans
vlans_E.extend(vlans2)
print("extend vlans=", vlans_E)
vlans_S = vlans2 + vlans
print("vlans summarized=", vlans_S)
print("vlans b pop=",vlans)
print("method pop", vlans.pop(-1))
print("vlans a pop =",vlans)
vlans.remove('300')
print("vlans a remove 300=",vlans)
vlans.insert(1, '10')
print("insert 10 =", vlans)
print("index 10 =", vlans.index('10'))
vlans.sort()
print("sort =", vlans)

#• Dictionaries (словари)
#• Tuples (кортежи)
#• Sets (множества)
#• Boolean (логический тип данных)
#Эти типы данных можно, в свою очередь, классифицировать по нескольким признакам:
#• изменяемые (списки, словари и множества)
#• неизменяемые (числа, строки и кортежи)
#• упорядоченные (списки, кортежи, строки и словари)
#• неупорядоченные (множества)