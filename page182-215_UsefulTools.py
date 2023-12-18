'''
Python for network engineers Natasha Samoilenko
'''
# Page range 182-215
# 8. Полезные возможности и инструменты
# Форматирование строк с помощью f-строк
ip = '10.1.1.1'
mask = 24
print(f"IP: {ip}, mask: {mask}")

octets = ['10', '1', '1', '1']
mask = 24
print(f"IP: {'.'.join(octets)}, mask: {mask}")

oct1, oct2, oct3, oct4 = [10, 1, 1, 1]
print(f'''
IP address:
        {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
        {oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}''')

# f-строки в циклах, f-строку надо писать в теле цикла, чтобы она «подхва-
# тывала» новые значения переменных на каждой итерации
ip_list = ['10.1.1.1/24', '10.2.2.2/24', '10.3.3.3/24']
for ip_address in ip_list:
    ip, mask = ip_address.split('/')
    print(f"IP: {ip}, mask: {mask}")

# Выравнивание столбцами:
topology = [['sw1', 'Gi0/1', 'r1', 'Gi0/2'],
            ['sw1', 'Gi0/2', 'r2', 'Gi0/1'],
            ['sw1', 'Gi0/3', 'r3', 'Gi0/0'],
            ['sw1', 'Gi0/5', 'sw4', 'Gi0/2']]
for connection in topology:
    l_device, l_port, r_device, r_port = connection
    print(f'{l_device:10} {l_port:7} {r_device:10} {r_port:7}')

print("Ширина столбцов может быть указана через переменную:")
topology = [['sw1', 'Gi0/1', 'r1', 'Gi0/2'],
            ['sw1', 'Gi0/2', 'r2', 'Gi0/1'],
            ['sw1', 'Gi0/3', 'r3', 'Gi0/0'],
            ['sw1', 'Gi0/5', 'sw4', 'Gi0/2']]
width = 10
for connection in topology:
    l_device, l_port, r_device, r_port = connection
    print(f"{l_device:{width}} {l_port:{width}} {r_device:{width}} {r_port:{width}}")

# Работа со словарями
session_stats = {'done': 10, 'todo': 5}
if session_stats['todo']:
    print(f"Pomodoros done: {session_stats['done']}, TODO: {session_stats['todo']}")
else:
    print(f"Good job! All {session_stats['done']} pomodoros done!")

# Вызов метода upper внутри f-строки:
name = 'python'
print(f'Zen of {name.upper()}')

# Вызов функции len внутри f-строки:
name = 'python'
print(f'Zen of {len(name)}')

# Что использовать format или f-строки
ip = [10, 1, 1, 1]
oct1, oct2, oct3, oct4 = ip
print(f'{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}')
template = "{:08b} " * 4  # когда вот так повторяется то первый шаблон можно создать
# с помощью f а потом задествовать его сколько нужно при помощи format()
template.format(oct1, oct2, oct3, oct4)


# функцию для вывода строки по шаблону:
def show_me_ip(ip, mask):
    return f"IP: {ip}, mask: {mask}"


print(show_me_ip('10.1.1.1', 24))
print(show_me_ip('192.16.10.192', 28))

# Распаковка переменных
interface = ['FastEthernet0/1', '10.1.1.1', 'up', 'up']
intf, ip, status, protocol = interface
print(intf, ip, status, protocol)
# Такой вариант намного удобней использовать, чем использование индексов:
intf, ip, status, protocol = interface[0], interface[1], interface[2], interface[3]
# Замена ненужных элементов _
intf, ip, _, _ = interface
intf, ip, *rest = interface  # Такая переменная со звездочкой в выражении распаковки может быть только одна и в любом месте(начало, конец, середина)

# Пример распаковки в цикле for
# Пример цикла, который проходится по ключам:
access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
access = {'0/12': 10, '0/14': 11, '0/16': 17}
for intf in access:
    print(f'interface FastEthernet {intf}')
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, access[intf]))
    else:
        print(' {}'.format(command))

# Пример распаковки элементов списка в цикле:
table = [
    ['100', 'a1b2.ac10.7000', 'DYNAMIC', 'Gi0/1'],
    ['200', 'a0d4.cb20.7000', 'DYNAMIC', 'Gi0/2'],
    ['300', 'acb4.cd30.7000', 'DYNAMIC', 'Gi0/3'],
    ['100', 'a2bb.ec40.7000', 'DYNAMIC', 'Gi0/4'],
    ['500', 'aa4b.c550.7000', 'DYNAMIC', 'Gi0/5'],
    ['200', 'a1bb.1c60.7000', 'DYNAMIC', 'Gi0/6'],
    ['300', 'aa0b.cc70.7000', 'DYNAMIC', 'Gi0/7']]
for vlan, mac, _, intf in table:
    print(vlan, mac, intf)

# List, dict, set comprehensions
items = ["10", "20", "30", "1", "11", "100"]
vlans = [int(vl) for vl in items]
print(vlans)

items = ['10', '20', 'a', '30', 'b', '40']
only_digits = []
for item in items:
    if item.isdigit():
        only_digits.append(int(item))
# Or
only_digits = [int(item) for item in items if item.isdigit()]
print(only_digits)

london_co = {
    'r1': {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101'
    }
}
print([london_co[device]['ios'] for device in london_co])
print([london_co[device]['ip'] for device in london_co])

vlans = [[10, 21, 35], [101, 115, 150], [111, 40, 50]]
result = []
for vlan_list in vlans:
    for vlan in vlan_list:
        result.append(vlan)
print(result)
# Or it is better
vlans = [[10, 21, 35], [101, 115, 150], [111, 40, 50]]
result = [vlan for vlan_list in vlans for vlan in vlan_list]
print(result)

# Dict comprehensions (генераторы словарей)
d = {}
for num in range(1, 11):
    d[num] = num ** 2
print(d)

d = {num: num ** 2 for num in range(1, 11)}
print(d)

# надо преобразовать существующий словарь и перевести все
# ключи в нижний регистр. Для начала, вариант решения
r1 = {'IOS': '15.4',
      'IP': '10.255.0.1',
      'Hostname': 'london_r1',
      'Location': '21 New Globe Walk',
      'Model': '4451',
      'Vendor': 'Cisco'}
# без генератора словаря:
lower_r1 = {}
for key, value in r1.items():
    lower_r1[key.lower()] = value
# генератор словаря:
lower_r1 = {key.lower(): value for key, value in r1.items()}
print(lower_r1)

# аналогично ключи во вложенных словаряхЖ
london_co = {
    'r1': {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101'
    }
}
lower_london_co = {}
# без генератора словаря:
for device, params in london_co.items():
    lower_london_co[device] = {}
    for key, value in params.items():
        lower_london_co[device][key.lower()] = value
# генератор словаря:
result = {}
result = {device: {key.lower(): value for key, value in params.items()}
          for device, params in london_co.items()}
print(result)

#Set comprehensions (генераторы множеств)
# генератор множества:
vlans = [10, '30', 30, 10, '56']
unique_vlans = {int(vlan) for vlan in vlans}
print(unique_vlans)
# без генератора множества:
unique_vlans = set()
for vlan in vlans:
    unique_vlans.add(int(vlan))

print("--ОТЛАДКА--"*5)
#Отладка с помощью print и разновидностей
#pprint - показывает выводит строки с кавычками,
# а числа нет, а так же показывает специальные символы
from pprint import pprint
pprint("100")
pprint(100)
line = "\nline1\t\nline2\r\n"
pprint(line)
# то же самое можно делать с print добавив repr
print(repr(line))

#ОТЛАДКА начиная с версии 3.8 - f"{var=}":
line = "\nline1\t\nline2"
item = "100"
#print(f"{line=} {item=}")
#for i in range(5):
#    print(f"{i=}")

#locals - показывает все локальные переменные. Если в коде нет функций, это будут
#все глобальные переменные, если сделать вывод внутри функции, только переменные этой функции.
from pprint import pprint
item = "100"
line = "\nline1\n\tline2"
print("---LOCALS---"*5)
pprint(locals())

#Пример кода с функцией:
print("Пример кода с функцией")
from pprint import pprint
def num_sum(x, y):
    result = x + y
    pprint(locals())
    return result
num_sum(10, 5)

#Breakpoint с условием
#Сделать breakpoint в строке 12, если значение переменной num будет больше 10:
#break 12, num > 10