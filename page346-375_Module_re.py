'''
Python for network engineers Natasha Samoilenko
'''
# Page range 346-375
# 15. Модуль re
import re

# 15.1 Объект Match
log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)', log)
print(match)
##group
###Метод group возвращает подстроку, которая совпала с выражением или с выражением в группе.
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(1, 2, 3))
log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'Host (\w{4}\.)+', log)
print(match.group(1))  # запоминается и возвращается только последнее выражение

log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'Host (?P<mac>\S+) '
                  r'in vlan (?P<vlan>\d+) .* '
                  r'port (?P<int1>\S+) '
                  r'and port (?P<int2>\S+)', log)
print(match.group('mac'))
print(match.group('int1'))
print(match.group(1, 2, 3))

##groups - Метод groups возвращает кортеж со строками
log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'Host (\S+) '
                  r'in vlan (\d+) .* '
                  r'port (\S+) '
                  r'and port (\S+)',
                  log)
print(match.groups())
line = '100 aab1.a1a1.a5d3 FastEthernet0/1'
match = re.search(r'(\d+) +(\w+)?', line)
print(match.groups())
line = '100 '
match = re.search(r'(\d+) +(\w+)?', line)
print(match.groups())
print(match.groups(default=0))
print(match.groups(default='No match'))

# groupdict
log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'Host (?P<mac>\S+) '
                  r'in vlan (?P<vlan>\d+) .* '
                  r'port (?P<int1>\S+) '
                  r'and port (?P<int2>\S+)',
                  log)
print(match.groupdict())

# start, end - Методы start и end возвращают индексы начала и конца совпадения с регулярным выражением.
line = ' 10 aab1.a1a1.a5d3 FastEthernet0/1 '
match = re.search(r'(\d+) +([0-9a-f.]+) +(\S+)', line)
print(match.start())
print(match.end())
print(line[match.start():match.end()])
# можно передавать номер или имя группы
print(match.start(2))
print(match.end(2))
print(line[match.start(2):match.end(2)])
# можно передавать имя группы
log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'Host (?P<mac>\S+) '
                  r'in vlan (?P<vlan>\d+) .* '
                  r'port (?P<int1>\S+) '
                  r'and port (?P<int2>\S+)',
                  log)
print(match.start('mac'))
print(match.end('mac'))
print(log[match.start(1):match.end(1)])
print(log[match.start('mac'):match.end('mac')])
###span возвращает кортеж с индексом начала и конца подстроки. Он работает анало-
###гично методам start, end, но возвращает пару чисел
print(match.span('mac'))
print(match.span(1))

# 15.2 Функция search
log = '%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24'
match = re.search(r'Host \S+ '
                  r'in vlan (\d+) '
                  r'is flapping between port '
                  r'(\S+) and port (\S+)', log)
print(match.groups())

regex = (r'Host \S+ '
         r'in vlan (\d+) '
         r'is flapping between port '
         r'(\S+) and port (\S+)')
ports = set()
with open('page_354_flapping_mac_log.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            vlan = match.group(1)
            ports.add(match.group(2))
            ports.add(match.group(3))
print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))

###Обработка вывода show cdp neighbors detail
import re
from pprint import pprint


def parse_cdp(filename):
    result = {}
    with open(filename) as f:
        for line in f:
            if line.startswith('Device ID'):
                neighbor = re.search(r'Device ID: (\S+)', line).group(1)
                result[neighbor] = {}
            elif line.startswith(' IP address'):
                ip = re.search(r'IP address: (\S+)', line).group(1)
                result[neighbor]['ip'] = ip
            elif line.startswith('Platform'):
                platform = re.search(r'Platform: (\S+ \S+),', line).group(1)
                result[neighbor]['platform'] = platform
            elif line.startswith('Cisco IOS Software'):
                ios = re.search(r'Cisco IOS Software, (.+), RELEASE', line).group(1)
                result[neighbor]['ios'] = ios
    return result


pprint(parse_cdp('page_356_sh_cdp_neighbors_sw1.txt'))

# 15.3 Функция match - отличается от search тем, что match всегда ищет совпадение в начале стро-ки.
log = '%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24'
match = re.match(r'Host \S+ '
                 r'in vlan (\d+) '
                 r'is flapping between port '
                 r'(\S+) and port (\S+)', log)
print(print(match))

regex = (r'\S+: Host \S+ '
         r'in vlan (\d+) '
         r'is flapping between port '
         r'(\S+) and port (\S+)')
ports = set()
with open('page_354_flapping_mac_log.txt') as f:
    for line in f:
        match = re.match(regex, line)
        if match:
            vlan = match.group(1)
            ports.add(match.group(2))
            ports.add(match.group(3))
print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))

# 15.4 Функция finditer - используется для поиска всех непересекающихся совпадений в шаблоне
##подходит если вывод которых отображается столбцами
sh_ip_int_br = '''
R1#show ip interface brief
Interface IP-Address OK? Method Status Protocol
FastEthernet0/0 15.0.15.1 YES manual up up
FastEthernet0/1 10.0.12.1 YES manual up up
FastEthernet0/2 10.0.13.1 YES manual up up
FastEthernet0/3 unassigned YES unset up up
Loopback0 10.1.1.1 YES manual up up
Loopback100 100.0.0.1 YES manual up up
'''

result = re.finditer(r'(\S+) +'
                     r'([\d.]+) +'
                     r'\w+ +\w+ +'
                     r'(up|down|administratively down) +'
                     r'(up|down)',
                     sh_ip_int_br)
groups = []
for match in result:
    print(match)
    groups.append(match.groups())
print(groups)

# Аналогичный результат можно получить с помощью генератора списков:
regex = r'(\S+) +([\d.]+) +\w+ +\w+ +(up|down|administratively down) +(up|down)'
result = [match.groups() for match in re.finditer(regex, sh_ip_int_br)]
print(result)

import re

regex = (r'Host \S+ '
         r'in vlan (\d+) '
         r'is flapping between port '
         r'(\S+) and port (\S+)')
ports = set()
with open('page_354_flapping_mac_log.txt') as f:
    for m in re.finditer(regex, f.read()):
        vlan = m.group(1)
        ports.add(m.group(2))
        ports.add(m.group(3))
print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))

import re
from pprint import pprint


def parse_cdp2(filename):
    regex = (r'Device ID: (?P<device>\S+)'
             r'|IP address: (?P<ip>\S+)'
             r'|Platform: (?P<platform>\S+ \S+),'
             r'|Cisco IOS Software, (?P<ios>.+), RELEASE')
    result = {}
    with open(filename) as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:
            if match.lastgroup == 'device':
                device = match.group(match.lastgroup)
                result[device] = {}
            elif device:
                result[device][match.lastgroup] = match.group(match.lastgroup)
    return result


pprint(parse_cdp2('page_356_sh_cdp_neighbors_sw1.txt'))

# 15.5 Функция findall():
# • используется для поиска всех непересекающихся совпадений в шаблоне
# • возвращает:
#  – список строк, которые описаны регулярным выражением, если в регулярном выражении нет групп
#  – список строк, которые совпали с регулярным выражением в группе, если в регулярном выражении одна группа
#  – список кортежей, в которых находятся строки, которые совпали с выражением в группе, если групп несколько

mac_address_table = open('CAM_table.txt').read()
print(mac_address_table)
print(re.findall(r'\d+ +\S+ +\w+ +\S+', mac_address_table))
print(re.findall(r'\d+ +(\S+) +\w+ +\S+', mac_address_table))
print(re.findall(r'(\d+) +(\S+) +\w+ +(\S+)', mac_address_table))

import re

regex = (r'Host \S+ '
         r'in vlan (\d+) '
         r'is flapping between port '
         r'(\S+) and port (\S+)')
ports = set()
with open('page_354_flapping_mac_log.txt') as f:
    result = re.findall(regex, f.read())
    for vlan, port1, port2 in result:
        ports.add(port1)
        ports.add(port2)
        ports.add(port2)
print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))

# 15.6 Функция compile - скомпилировать регулярное выражение, а затем использовать его.
# Это особенно полезно в тех случаях, когда регулярное выражение много используется в скрипте.
regex = re.compile(r'\d+ +\S+ +\w+ +\S+')
line = ' 100 a1b2.ac10.7000 DYNAMIC Gi0/1'
match = regex.search(line)
print(match)
print(match.group())
print(match.groups())
regex = re.compile(r'^Device ID: \S+.+?Cisco IOS', re.MULTILINE | re.DOTALL)
match_all = regex.finditer(line)
print(match_all)

import re

regex = re.compile(r'Host \S+ '
                   r'in vlan (\d+) '
                   r'is flapping between port '
                   r'(\S+) and port (\S+)')
ports = set()
with open('page_354_flapping_mac_log.txt') as f:
    for m in regex.finditer(f.read()):
        vlan = m.group(1)
        ports.add(m.group(2))
        ports.add(m.group(3))
print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))

# Параметры, которые доступны только при использовании re.compile
# При использовании функции re.compile в методах search, match, findall, finditer и fullmatch
# появляются дополнительные параметры:
# • pos - позволяет указывать индекс в строке, с которого надо начать искать совпадение
# • endpos - указывает, до какого индекса надо выполнять поиск
regex = re.compile(r'\d+ +\S+ +\w+ +\S+')
line = ' 100 a1b2.ac10.7000 DYNAMIC Gi0/1'
match = regex.search(line)
print(match.group())

###указывается начальная позиция поиска:
match = regex.search(line, 2)
print(match.group())

###Указание начальной позиции аналогично срезу строки:
match = regex.search(line[2:])
print(match.group())

###использование двух индексов:
line = ' 100 a1b2.ac10.7000 DYNAMIC Gi0/1'
regex = re.compile(r'\d+ +\S+ +\w+ +\S+')
match = regex.search(line, 2, 40)
print(match.group())

###срез строки:
match = regex.search(line[2:40])
print(match.group())

# 15.7 Флаги
### re.ASCII (re.A)
### re.IGNORECASE (re.I)
### re.MULTILINE (re.M)
### re.DOTALL (re.S)
### re.VERBOSE (re.X)
### re.LOCALE (re.L)
### re.DEBUG

with open('sh_cdp_n_sw1.txt') as f:
    sh_cdp = f.read()
    regex = r'Device ID: (\S+).+?Platform: \w+ (\S+),.+?Cisco IOS Software.+? Version(\S +), '
    match = re.finditer(regex, sh_cdp, re.DOTALL)
    for m in match:
        print(m.groups())

# 15.8 Функция re.split - аналогично методу split в строках
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
print(re.split(r' +', ospf_route))
print(re.split(r'[ ,]+', ospf_route))
print(re.split(r'[ ,\[\]]+', ospf_route))
print(re.split(r'(via|[ ,\[\]])+', ospf_route))  # попадает разделитель, чтоб это отключить
# надо сделать группу noncapture. То есть, отключить запоминание элементов группы:
print(re.split(r'(?:via|[ ,\[\]])+', ospf_route))

# 15.9 Функция re.sub - аналогично методу replace в строках
print(re.sub(r'(via|[,\[\]])', ' ', ospf_route))
mac_table = '''
100 aabb.cc10.7000 DYNAMIC Gi0/1
200 aabb.cc20.7000 DYNAMIC Gi0/2
300 aabb.cc30.7000 DYNAMIC Gi0/3
100 aabb.cc40.7000 DYNAMIC Gi0/4
500 aabb.cc50.7000 DYNAMIC Gi0/5
200 aabb.cc60.7000 DYNAMIC Gi0/6
300 aabb.cc70.7000 DYNAMIC Gi0/7
'''
print(re.sub(r' *(\d+) +'
             r'([a-f0-9]+)\.'
             r'([a-f0-9]+)\.'
             r'([a-f0-9]+) +\w+ +'
             r'(\S+)',
             r'\1 \2:\3:\4 \5',
             mac_table))
