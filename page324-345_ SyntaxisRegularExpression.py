'''
Python for network engineers Natasha Samoilenko
'''
# Page range 324-345
# 14. Синтаксис регулярных выражений
import re  # для работы с регулярными выражениями используется модуль re.

print(r"\\data")  # Raw-строки
print('\\\\data')  # экранирование символов
# функции search:
int_line = ' MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
match = re.search(r'MTU', int_line)
print(match)
print(match.group())
print(re.search(r'M_U', int_line))
match = re.search(r'BW \d+', int_line)
print(match.group())
log2 = 'Oct 3 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6 in vlan 1 is flapping between port Gi0/5 and port Gi0/16'
print(re.search(r'Host (\S+) in vlan (\d+) is flapping between port (\S+) and port (\S+)', log2).groups())
###• \d - любая цифра
###• \D - любое нечисловое значение
###• \s - пробельные символы
###• \S - все, кроме пробельных символов
###• \w - любая буква, цифра или нижнее подчеркивание
###• \W - все, кроме букв, цифр или нижнего подчеркивания
log = '*Jul 7 06:15:18.695: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down'
print(re.search(r'\d\d:\d\d:\d\d', log).group())
print(re.search(r'\w\w\w\w\.\w\w\w\w\.\w\w\w\w', log2).group())
###Символы повторения
###• regex+ - одно или более повторений предшествующего элемента
###• regex* - ноль или более повторений предшествующего элемента
###• regex? - ноль или одно повторение предшествующего элемента
###• regex{n} - ровно n повторений предшествующего элемента
###• regex{n,m} - от n до m повторений предшествующего элемента
###• regex{n,} - n или более повторений предшествующего элемента
line = '100 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.search(r'a+', line).group())
print(re.search(r'(a1)+', line).group())
sh_ip_int_br = 'Ethernet0/1 192.168.200.1 YES NVRAM up up'
print(re.search(r'\d+\.\d+\.\d+\.\d+', sh_ip_int_br).group())
line = '1500 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.search(r'\d+\s+\S+', line).group())
print(re.search(r'ba*', line).group())
line = '100 a011.baaa.a5d3 FastEthernet0/1'
print(re.search(r'ba*', line).group())
email1 = 'user1@gmail.com'
print(re.search(r'\w+@\w+\.\w+', email1).group())
email2 = 'user2.test@gmail.com'
print(re.search(r'\w+@\w+\.\w+', email2).group())
print(re.search(r'\w+\.\w+@\w+\.\w+', email2).group())
print(re.search(r'\w+\.*\w+@\w+\.\w+', email1).group())
print(re.search(r'\w+\.*\w+@\w+\.\w+', email2).group())

mail_log = ['Jun 18 14:10:35 client-ip=154.10.180.10 from=user1@gmail.com,size=551',
            'Jun 18 14:11:05 client-ip=150.10.180.10 from=user2.test@gmail.com,size=768']
for message in mail_log:
    match = re.search(r'\w+\.?\w+@\w+\.\w+', message)
    if match:
        print("Found email: ", match.group())

line = '100 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.search(r'\w{4}\.\w{4}\.\w{4}', line).group())

mac_table = '''
			sw1#sh mac address-table
			Mac Address Table
			-------------------------------------------

			Vlan Mac Address Type Ports
			---- ----------- -------- -----
			100 a1b2.ac10.7000 DYNAMIC Gi0/1
			200 a0d4.cb20.7000 DYNAMIC Gi0/2
			300 acb4.cd30.7000 DYNAMIC Gi0/3
			1100 a2bb.ec40.7000 DYNAMIC Gi0/4
			500 aa4b.c550.7000 DYNAMIC Gi0/5
			1200 a1bb.1c60.7000 DYNAMIC Gi0/6
			1300 aa0b.cc70.7000 DYNAMIC Gi0/7
			'''
for line in mac_table.split('\n'):
    match = re.search(r'\d{1,4} +', line)
    if match:
        print('VLAN: ', match.group())
### . 		- любой символ, кроме символа новой строки
### ^ 		- начало строки
### $ 		- конец строки
### [abc] 	- любой символ в скобках
### [^abc] 	- любой символ, кроме тех, что в скобках
### a|b 	- элемент a или b
### (regex) - выражение рассматривается как один элемент. Кроме того, подстрока, которая совпала с выражением, запоминается
cdp = '''
	  SW1#show cdp neighbors detail
	  -------------------------
	  Device ID: SW2
	  Entry address(es):
	  IP address: 10.1.1.2
	  Platform: cisco WS-C2960-8TC-L, Capabilities: Switch IGMP
	  Interface: GigabitEthernet1/0/16, Port ID (outgoing port): GigabitEthernet0/1
	  Holdtime : 164 sec
	  '''
print(re.search(r'Interface.+Port ID.+', cdp).group())
line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'^\d+', line).group())
prompt = 'SW1#show cdp neighbors detail'
print(re.search(r'^.+#', prompt).group())
line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'\S+$', line).group())
line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[Ff]ast', line).group())
print(re.search(r'[Ff]ast[Ee]thernet', line).group())
commands = ['SW1#show cdp neighbors detail',
            'SW1>sh ip int br',
            'r1-london-core# sh ip route']
for line in commands:
    match = re.search(r'^.+[>#]', line)
    if match:
        print(match.group())
line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'[0-9]+', line).group())
print(re.search(r'[a-z]+', line).group())
print(re.search(r'[A-Z]+', line).group())
print(re.search(r'[a-f0-9]+\.[a-f0-9]+\.[a-f0-9]+', line).group())
print(re.search(r'[a-f0-9]+[./][a-f0-9]+', line).group())
line = 'FastEthernet0/0 15.0.15.1 YES manual up up'
print(re.search(r'[^a-zA-Z]+', line).group())
line = "100 aa12.35fe.a5d3 FastEthernet0/1"
print(re.search(r'Fast|0/1', line).group())
print(re.search(r'[0-9]([a-f]|[0-9])[0-9]', line).group())
line = 'FastEthernet0/0 15.0.15.1 YES manual up up'
print(re.search(r'([0-9]+\.)+[0-9]+', line).group())

# Жадность символов повторения
line = '<text line> some text>'
match = re.search(r'<.*>', line)
print(match.group())
match = re.search(r'<.*?>', line)  # отключить жадность - знак вопроса после символов повторения
print(match.group())
line = '1500 aab1.a1a1.a5d3 FastEthernet0/1'
print(re.search(r'\d+\s+\S+', line).group())
print(re.search(r'\d+\s+\S+?', line).group())

# Группировка выражений
##Нумерованные группы
line = "FastEthernet0/1 10.0.12.1 YES manual up up"
match = re.search(r'(\S+)\s+([\w.]+)\s+.*', line)
print(match.group(0))
print(match.group(1))
print(match.group(2))
# print(match.group(3))
print(match.group(2, 1, 2))
print(match.group(1, 2))
print(match[0])
print(match[1])
print(match[2])
print(match.groups())

##Именованные группы
####Синтаксис именованной группы (?P<name>regex):
line = "FastEthernet0/1 10.0.12.1 YES manual up up"
match = re.search(r'(?P<intf>\S+)\s+(?P<address>[\d.]+)\s+', line)
print(match.group('intf'))
print(match.group('address'))
print(match.groupdict())
match = re.search(r'(?P<intf>\S+)\s+(?P<address>[\d\.]+)\s+\w+\s+\w+\s+(?P<status>up|down)\s+(?P<protocol>up|down)',
                  line)
print(match.groupdict())

# show ip dhcp snooping с помощью именованных групп
dhcp_snooping = """
MacAddress IpAddress Lease(sec) Type VLAN Interface
------------------ ------------ ---------- ------------- ---- --------------------
00:09:BB:3D:D6:58 10.1.10.2 86250 dhcp-snooping 10 FastEthernet0/1
00:04:A3:3E:5B:69 10.1.5.2 63951 dhcp-snooping 5 FastEthernet0/10
00:05:B3:7E:9B:60 10.1.5.4 63253 dhcp-snooping 5 FastEthernet0/9
00:09:BC:3F:A6:50 10.1.10.6 76260 dhcp-snooping 10 FastEthernet0/3
Total number of bindings: 4
"""
line = '00:09:BB:3D:D6:58 10.1.10.2 86250 dhcp-snooping 10 FastEthernet0/1'
match = re.search(r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<port>\S+)', line)
print(match.groupdict())

regex = r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<port>\S+)'
result = []
with open('page_342_dhcp-snooping.txt') as data:
    for line in data:
        match = re.search(regex, line)
        if match:
            result.append(match.groupdict())
            print('К коммутатору подключено {} устройства'.format(len(result)))
    for num, comp in enumerate(result, 1):
        print('Параметры устройства {}:'.format(num))
        for key in comp:
            print('{:10}: {:10}'.format(key, comp[key]))

# Группа без захвата
log = 'Jun 3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'((\w{4}\.){2}\w{4}).+vlan (\d+).+port (\S+).+port (\S+)', log)
print(match.groups())
# отключить захват в группе. Это делается добавлением ?: после открывающейся скобки группы
match = re.search(r'((?:\w{4}\.){2}\w{4}).+vlan (\d+).+port (\S+).+port (\S+)', log)
print(match.groups())

# Повторение захваченного результата
bgp = '''
R9# sh ip bgp | be Network
Network Next Hop Metric LocPrf Weight Path
* 192.168.66.0/24 192.168.79.7 0 500 500 500 i
*> 192.168.89.8 0 800 700 i
* 192.168.67.0/24 192.168.79.7 0 0 700 700 700 i
*> 192.168.89.8 0 800 700 i
* 192.168.88.0/24 192.168.79.7 0 700 700 700 i
*> 192.168.89.8 0 0 800 800 i
'''
#выводит если AS повторяется 2 раза
for line in bgp.split('\n'):
    match = re.search(r'(\d+) \1', line)# \1 - указывает на повторение еще раз результата из первой группы (\d+), тут только одна группа
    if match:
        print(line)
#выводит если AS повторяется 3 раза
for line in bgp.split('\n'):
    match = re.search(r'(\d+) \1 \1', line)
    if match:
        print(line)

#Аналогичным образом можно ссылаться на результат, который попал в именованную группу:
for line in bgp.split('\n'):
	match = re.search(r'(?P<as>\d+) (?P=as)', line)#подставляет еще раз полученный результат из группы as
	if match:
		print(line)