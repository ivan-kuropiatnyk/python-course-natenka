'''
Python for network engineers Natasha Samoilenko
'''
# Page range 290 - 313
# 12. Полезные модули
##• subprocess
import subprocess

result = subprocess.run('ls', shell=True)
print(result)
asdf = result.returncode
print(asdf)
result1 = subprocess.run(['ls', '-halF'], shell=True)
print(result1)
result2 = subprocess.run('ls -halF *py', shell=True)
print(result2)
result3 = subprocess.run(['ping', '-c', '1', '-n', '8.8.8.8'])
print(result3)
result4 = subprocess.run(['ls -F'], stdout=subprocess.PIPE, shell=True, encoding='utf-8')
print(result4.stdout)
result5 = subprocess.run(['ls', '-lsF'], stdout=subprocess.PIPE)
print("result 5 =>", result5.stdout)
print("result 5 decoded =>\n", result5.stdout.decode('utf-8'))
result6 = subprocess.run(['ls', '-ls'], stdout=subprocess.PIPE, encoding='utf-8')
print("\n result 6 =>\n", result6.stdout)

# отключить вывод результата выполнения на стандартный поток вывода
result7 = subprocess.run(['ls', '-ls'], stdout=subprocess.DEVNULL)
print("\n result 7 =>\n", result7.stdout)

# Работа со стандартным потоком ошибок
result8 = subprocess.run(['ping', '-c', '3', '-n', 'a'], stderr=subprocess.PIPE, encoding='utf-8')
print("\n result 8 =>\n", result8.stdout)
print("\n result 8 =>\n", result8.stderr)

# Примеры использования модуля
reply = subprocess.run(['ping', '-c', '1', '-n', '8.8.8.8'])
if reply.returncode == 0:
    print('Alive')
else:
    print('Unreachable')


def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
    * True
    * command output (stdout)
    On failure:
    * False
    * error output (stderr)
    """
    reply = subprocess.run(['ping', '-c', '1', '-n', ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stderr


print(ping_ip('8.8.8.8'))
print(ping_ip('a'))

##• os
import os

print(os.environ)
print(os.environ["HOME"])
# print(os.environ["TOKEN"])#here is error message
print(os.environ.get("HOME"))
print(os.environ.get("TOKEN"))

# os.mkdir('test2')#it created already a test folder andgives an error because test folder exists already
result9 = subprocess.run(['ls -F | egrep test'], stdout=subprocess.PIPE, shell=True, encoding='utf-8')
print("\n result 9 =>\n", result9.stdout)

result10 = os.listdir("/home")  # gives a list of folders and files inside folder /home
print("\n result 10 =>\n", result10)
print(sorted(os.listdir("/home")))
print(os.listdir('.'))  # currenct directory
print(os.listdir())  # currenct directory also

print(os.path.exists('test'))
if not os.path.exists('test'):
    os.mkdir('test')

# Функция os.path.isdir возвращает True, если путь ведет к каталогу и False иначе:
print(os.path.isdir('test'))
print(os.path.isdir('testADS'))

# Функция os.path.isfile возвращает True, если путь ведет к файлу и False иначе:
print(os.path.isfile('test'))

dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
print(dirs)
files = [d for d in os.listdir() if os.path.isfile(d)]
print(files)

# os.path.split делает разделение пути на «основную часть» и конец пути по последнему / и возвращает кортеж из двух элементов
print(os.path.split("./test"))
print(os.path.split("./test/"))
print(os.path.split("/home/ivankurop/PycharmProjects/pythonProjectNata1/test/test.txt"))
print(os.path.split("/home/ivankurop/PycharmProjects/pythonProjectNata1/test"))
print(os.path.split("/home/ivankurop/PycharmProjects/pythonProjectNata1/test/"))

print(os.path.abspath("./test/test.txt"))

##• ipaddress
import ipaddress

ipadd_v4 = ipaddress.ip_address('10.0.1.1')
print(ipadd_v4)

print(ipadd_v4.is_loopback)
print(ipadd_v4.is_multicast)
print(ipadd_v4.is_reserved)
print(ipadd_v4.is_private)

ip1 = ipaddress.ip_address('10.0.1.1')
ip2 = ipaddress.ip_address('10.0.2.1')
print("ip1 > ip2 =", ip1 > ip2)
print("ip2 > ip1 =", ip2 > ip1)
print("ip1 == ip2 =", ip1 == ip2)
print("ip1 != ip2 =", ip1 != ip2)
print("str(ip1) =", str(ip1))
print("int(ip1) =", int(ip1))
print("ip1 + 5 =", ip1 + 5)
print("ip1 - 5 =", ip1 - 5)

###ipaddress.ip_network - Функция ipaddress.ip_network позволяет
###создать объект, который описывает сеть (IPv4 или IPv6):
subnet1 = ipaddress.ip_network('80.0.1.0/28')
print("broadcast => ", subnet1.broadcast_address)
print("netmask => ", subnet1.with_netmask)
print("netmask => ", subnet1.with_netmask)
print("hostmask => ", subnet1.with_hostmask)
print("prefixlen => ", subnet1.prefixlen)
print("num_addresses => ", subnet1.num_addresses)

print(list(subnet1.hosts()))
print(list(subnet1.subnets()))
print(list(subnet1.subnets(prefixlen_diff=2)))  # split by quantity of bits in the subnet
print(list(subnet1.subnets(new_prefix=29)))  # split by new subnet mask

for ip in subnet1:
    print(ip)
print(subnet1[5])

ip1 = ipaddress.ip_address('80.0.1.3')
print(ip1 in subnet1)

##ipaddress.ip_interface
###Функция ipaddress.ip_interface позволяет создавать объект IPv4Interface или IPv6Interface соответственно:
int1 = ipaddress.ip_interface('10.0.1.1/24')
print(int1.ip)
print(int1.network)
print(int1.netmask)

###ПРИМЕР
IP1 = '10.0.1.1/24'
IP2 = '10.0.1.0/24'
def check_if_ip_is_network(ip_address):
    try:
        ipaddress.ip_network(ip_address)
        return True
    except ValueError:
        return False
print(check_if_ip_is_network(IP1))
print(check_if_ip_is_network(IP2))


##• tabulate
from tabulate import tabulate
sh_ip_int_br = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
				('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
				('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
				('Loopback0', '10.1.1.1', 'up', 'up'),
				('Loopback100', '100.0.0.1', 'up', 'up')]
print(tabulate(sh_ip_int_br))

###headers
columns = ['Interface', 'IP', 'Status', 'Protocol']
print(tabulate(sh_ip_int_br, headers=columns))

###Достаточно часто первый набор данных - это заголовки. Тогда достаточно указать headers равным «firstrow»:
data=[('Interface', 'IP', 'Status', 'Protocol'),
('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
('Loopback0', '10.1.1.1', 'up', 'up'),
('Loopback100', '100.0.0.1', 'up', 'up')]
print(tabulate(data, headers='firstrow'))

####данные в виде списка словарей, надо указать headers равным «keys»
list_of_dict = [{'IP': '15.0.15.1',
'Interface': 'FastEthernet0/0',
'Protocol': 'up',
'Status': 'up'},
{'IP': '10.0.12.1',
'Interface': 'FastEthernet0/1',
'Protocol': 'up',
'Status': 'up'},
{'IP': '10.0.13.1',
'Interface': 'FastEthernet0/2',
'Protocol': 'up',
'Status': 'up'},
{'IP': '10.1.1.1',
'Interface': 'Loopback0',
'Protocol': 'up',
'Status': 'up'},
{'IP': '100.0.0.1',
'Interface': 'Loopback100',
'Protocol': 'up',
'Status': 'up'}]
print(tabulate(list_of_dict, headers='keys'))

vlans = {"sw1": [10, 20, 30, 40], "sw2": [1, 2, 10], "sw3": [1, 2, 3, 4, 5, 10, 11, 12]}
print(tabulate(vlans, headers="keys"))

####Стиль таблицы
print(tabulate(list_of_dict, headers='keys', tablefmt="grid"))
print(tabulate(list_of_dict, headers='keys', tablefmt="pipe"))
print(tabulate(list_of_dict, headers='keys', tablefmt='html'))

####Выравнивание столбцов
print(tabulate(list_of_dict, headers='keys', tablefmt='pipe', stralign='center'))

##• pprint
london_co = {'r1': {'hostname': 'london_r1', 'location': '21 New Globe Walk',
                    'vendor': 'Cisco', 'model': '4451', 'IOS': '15.4', 'IP': '10.255.0.1'},
             'r2': {'hostname': 'london_r2', 'location': '21 New Globe Walk',
                    'vendor': 'Cisco', 'model': '4451', 'IOS': '15.4', 'IP': '10.255.0.2'},
             'sw1': {'hostname': 'london_sw1', 'location': '21 New Globe Walk', 'vendor': 'Cisco',
                     'model': '3850', 'IOS': '3.6.XE', 'IP': '10.255.0.101'}}

from pprint import pprint
pprint(london_co)

interfaces = [['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up'],
              ['FastEthernet0/1', '10.0.1.1', 'YES', 'manual', 'up', 'up'],
              ['FastEthernet0/2', '10.0.2.1', 'YES', 'manual', 'up', 'down']]
pprint(interfaces)

tunnel = '\ninterface Tunnel0\n ip address 10.10.10.1 255.255.255.0\n ip mtu 1416\n ip, ospf hello-interval 5\n tunnel source FastEthernet1/0\n tunnel protection ipsec profile,→DMVPN\n'
pprint(tunnel)

# depth in pprint
result = {
'interface Tunnel0': [' ip unnumbered Loopback0',
' tunnel mode mpls traffic-eng',
' tunnel destination 10.2.2.2',
' tunnel mpls traffic-eng priority 7 7',
' tunnel mpls traffic-eng bandwidth 5000',
' tunnel mpls traffic-eng path-option 10 dynamic',
' no routing dynamic'],
'ip access-list standard LDP': [' deny 10.0.0.0 0.0.255.255',
' permit 10.0.0.0 0.255.255.255'],
'router bgp 100': {' address-family vpnv4': [' neighbor 10.2.2.2 activate',
' neighbor 10.2.2.2 send-community both',
' exit-address-family'],
' bgp bestpath igp-metric ignore': [],
' bgp log-neighbor-changes': [],
' neighbor 10.2.2.2 next-hop-self': [],
' neighbor 10.2.2.2 remote-as 100': [],
' neighbor 10.2.2.2 update-source Loopback0': [],
' neighbor 10.4.4.4 remote-as 40': []},
'router ospf 1': [' mpls ldp autoconfig area 0',
' mpls traffic-eng router-id Loopback0',
' mpls traffic-eng area 0',
' network 10.0.0.0 0.255.255.255 area 0']}
pprint(result, depth=1)
pprint(result, depth=2)

#pformat - это функция, которая отображает результат в виде строки
from pprint import pformat
formatted_result = pformat(result)
print(formatted_result)

r1 = {"ios": "16.4", "hostname": "R1", "ip": "10.1.1.1", "vendor": "Cisco IOS"}
pprint(r1)
pprint(r1, sort_dicts=False)