'''
Python for network engineers Natasha Samoilenko
'''
# Page range 127-141
#if/elif/else
a = 15
if a == 10:
    print("a Equal to 10")
elif a < 10:
    print("a is Lower than 10")
else:
    print("a is Higher than 10")

#True и False:
list_to_test = [10, 20, 30, 40, 50, 60, 70]
if len(list_to_test) != 0:
    print("Length:", len(list_to_test))
    print("there are some objects")

#Оператор in
r1 = {
        'IOS': '15.4',
        'IP': '10.255.0.1',
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'model': '4451',
        'vendor': 'Cisco'
    }
a = 'IOS' in r1
b = '4451' in r1
print(a,b)

#Пример использования конструкции if/elif/else
username = "ivan"
password = "asdffdassdf"
if len(password) < 8:
    print("Password is to short")
elif username in password:
    print("password contain username")
else:
    print("Password for {} accepted".format(username))

#Ternary expression
s = [1, 2, 3, 4]
result = True if len(s) > 5 else False
print(result)

words = ['list', 'dict', 'tuple']
upper_words = []
#upper_words.append(words[0].upper())
for word in words:
    upper_words.append(word.upper())
print(upper_words)

for word in 'Test string'.split(' '):
    print(word.swapcase())

for i in range(10):
    print(f'interface FastEthernet0/{i}')

vlans = [10, 20, 30, 40, 100]
for vlan in vlans:
    print(f'vlan {vlan}')
    print(f'  name VLAN{vlan}')

r1 = {
'ios': '15.4',
'ip': '10.255.0.1',
'hostname': 'london_r1',
'location': '21 New Globe Walk',
'model': '4451',
'vendor': 'Cisco'}
for k in r1:
    print(k)
for pair in r1:
    print(pair+"="+r1[pair])
### OR
print("-------Or this code with item()----------")
for i1, i2 in r1.items():
    print(i1+"="+i2)
print(r1.items())

commands = ['switchport mode access', 'spanning-tree portfast', 'spanning-tree', 'bpduguard enable']
fast_int = ['0/1','0/3','0/4','0/7','0/9','0/10','0/11']
for fa in fast_int:
    print(f"interface Fa{fa}")
    for command in commands:
        print('  {}'.format(command))

access_template = [ 'switchport mode access',
                    'switchport access vlan',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']
access = {'0/12': 10, '0/14': 11, '0/16': 17, '0/17': 150}

for interface in access:
    print("interface Fa"+interface)
    for template in access_template:
        print(" "+template)
        if template == access_template[1]:
            print(" "+access_template[1]+" "+str(access[interface]))#access[interface]=vlan

a = 5
while a > 0:
    a -= 1
    print(a)

b = 5
c = -1
while (b-1) != c:
    c += 1
    print("   ",c)

#page 141
#цикл while полезен, так как он возвращает скрипт снова в начало проверок,
#позволяет снова набрать пароль, но при этом не требует перезапуска самого скрипта.
# -*- coding: utf-8 -*-
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
password_correct = False
while not password_correct:
    if len(password) < 8:
        print("Password is short")
        password = input('Введите пароль повторно: ')
    elif username in password:
        print(f"Password contains username {username}")
        password = input('Введите пароль повторно: ')
    else:
        print(f'Пароль для пользователя {username} установлен')
        password_correct = True