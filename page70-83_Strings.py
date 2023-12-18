'''
Python for network engineers Natasha Samoilenko
'''
# Page range 70 - 83

### type data
##### Page 70
#• Strings (строки)
tunnel10 = """
interface Tunnel10
ip address 10.10.10.10 255.255.255.0
ip mtu 1416
ip ospf hello-interval 5
tunnel source FastEthernet1/0
tunnel protection ipsec profile DMVPN
"""
print(tunnel10)
tunnel20 = '\ninterface Tunnel0\n ip address 10.10.10.20 255.255.255.0\n ip mtu 1416\n ip ospf hello-interval 5\n tunnel source FastEthernet1/0\n tunnel protection ipsec profile DMVPN'
print(tunnel20)

intf = 'interface'
type_intf = 'FastEthernet'
num_intf = "0/"
for i in range(6):
    print(intf+" "+type_intf+num_intf+str(i))

intf_5x = 5*(" "+intf)
reshetka = "#"*10
letter3 = intf[2] #this is 3rd letter of the string value = intf
print("intf_5x = "+intf_5x)
print("reshetka = "+reshetka)
print("letter3 = "+letter3)
print("-1 letter = "+intf[-1])
print("3: letter = "+intf[3:])
print("3:6 letter = "+intf[3:6])
print(":2 letter = "+intf[:2])
print("::2 letter = "+intf[::2])
print("::1 letter = "+intf[::1])
print("::3 letter = "+intf[::3])
print(":: letter = "+intf[::-1])
print(":: letter = "+intf[::])
print("length = "+str(len(intf)))

vlans = ['10', '20', '30', '40']
print("vlans =>",vlans)
print("function join vlans =>", ','.join(vlans))

string1 = 'FastEthernet'
string2 = 'tunnel 0'
print("upper(string1) ="+string1.upper())
print("lower(string1) ="+string1.lower())
print("swapcase(string1) ="+ string1.swapcase())
print("capitalize(string2) =", string2.capitalize())

string3 = 'Hello, hello, hello, hello'
print("string3.count('') =", string3.count(''))
print("string3.count('hello') =", string3.count('hello'))
print("string3.count('Hello') =", string3.count('Hello'))
print("string3.count('.') =", string3.count('.'))
print("string3.count(',') =", string3.count(','))

string_F = 'interface FastEthernet0/1'
print("string_F.find('Fast')=>", string_F.find('Fast'))
print("PRINT STARTING FAST TO THE END => " + string_F[string_F.find('Fast')::])
if string_F.find('Fast') > 0:
    print("It contain the word => " + string_F[string_F.find('Fast')::])
else:
    print("Did not find a word FAST ")
print("startswith()", string_F.startswith('inter'))
print("startswith()", string_F.startswith('0/1'))
print("startswith()", string_F.startswith(('0','1','i')))
print("endswith()", string_F.endswith('0/1'))
print("endswith()", string_F.endswith('Fast'))
print("endswith()", string_F.endswith(('0','1','i')))

string_R = string_F.replace('Fast', 'Gigabit')
print("string_R => " + string_R)

string_SB = '[\n\tinterface FastEthernet0/1\n]'
string_SA1 = string_SB.strip()
string_SA2 = string_SB.strip('[]')
string_SA3 = string_SB.lstrip('[]')
print("string_SB => " + string_SB)
print("string_SA1 => " + string_SA1)
print("string_SA2 => " + string_SA2)
print("string_SA3 => " + string_SA3)

string_SPLIT = 'switchport trunk allowed vlan 10,20,30,100-200'
print(string_SPLIT.split())
IP_SPLIT = "192.168.100.1"
print(IP_SPLIT.split("."))
sh_ip_int_br = "FastEthernet0/0 15.0.15.1 YES manual up up"
print(sh_ip_int_br.split())

##formating strings
string_format1 = "interface FastEthernet0/{}".format('1')
print("string_format1 =>", string_format1)
print('format ip = {}'.format('10.1.1.1'))
print('format number 100 = {}'.format(100))
print('format numbers 10, 1, 1,1 = {}'.format([10, 1, 1, 1]))
print("Format with 3decimels = {:.3f}".format(10.0/3))
print('IP TO 2x metric = {:b} {:b} {:b} {:b}'.format(192, 100, 1, 1))
print('IP TO 2x metric with zeros = {:08b} {:08b} {:08b} {:08b}'.format(192, 100, 1, 1))
print('{ip}/{mask}'.format(mask=24, ip='10.1.1.1'))
print('{1}/{0}'.format(24, '10.1.1.1'))
ip_template = '''
IP address:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
'''
print(ip_template.format(192, 100, 1, 1, 192, 100, 1, 1))

ip_template = '''
IP address2:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(192, 100, 1, 1))

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