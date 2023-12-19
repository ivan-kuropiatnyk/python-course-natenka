'''
Python for network engineers Natasha Samoilenko
'''
# Page range 108
### type data
# Основы сортировки данных
data = [[1, 100, 1000], [2, 2, 2], [1, 2, 3], [4, 100, 3]]
ip_list = ["10.1.1.1", "10.1.10.1", "10.1.2.1", "10.1.11.1"]
vlans = ['1', '30', '11', '3', '10', '20', '30', '100']
print(type(data))
print(sorted(data))
print(sorted(vlans))
print(sorted(ip_list))
#Задание 4.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat = nat.replace('FastEthernet0/1', 'GigabitEthernet0/1')
print("Задание 4.1 => \n",nat)
#Задание 4.2
mac = "AAAA:BBBB:CCCC"
mac = mac.replace(':','.')
print("Задание 4.2 => \n",mac)
#Задание 4.3
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config_split = config.split()
result = config_split[-1].split(",")
#result = config.split()[-1].split(",") #tak v otvete
print("Задание 4.3 => \n",result)

#Задание 4.4
vlans4 = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result4 = sorted(set(vlans4))
result4 = list(result4)
result4 = str(result4).replace(',','').replace('[','').replace(']','').split()
result4 = list(result4)
print(type(result4))
print("Задание 4.4 => \n",result4)

#Задание 4.5
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1 = command1.split()
command2 = command2.split()
command = command1[-1].split(",") + command2[-1].split(",")
command = sorted(set(command))
result = list(command)
print(type(result))
print("Задание 4.5 => \n",result)
#otvet
#vlans1 = command1.split()[-1].split(",")
#vlans2 = command2.split()[-1].split(",")
#result = sorted(set(vlans1) & set(vlans2))

#Задание 4.6
ospf_route = " 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
d_keys = ['Prefix','AD/Metric','Next-Hop','Last update','Outbound Interface']
dict1 = dict.fromkeys(d_keys)
ospf_route = ospf_route.replace('[','').replace(']','').replace('via','')
ospf_route = list(ospf_route.split())
dict1 = dict(zip(d_keys,ospf_route))
print("Задание 4.6 => \n",dict1)

#Задание 4.7
mac = "AAAA:BBBB:CCCC"
mac = list(mac.replace(':',''))
mac = [int(x,16) for x in mac]
print("Задание 4.5 => \n")
for i in mac:
    j = 0
    j = j + 1
    mac1 = "{0:04b}"
    mac1 = mac1.format(i)
    mac2 = print(mac1, end="")
    if j == 15:
        break
print("\n")
#otvet: bin_mac = "{:b}".format(int(mac.replace(":", ""), 16))

#Задание 4.8
ip      = "192.168.3.1"
ip_list = list(ip.split("."))
ip_list = [int(x) for x in ip_list]
ip_print = f'''
            IP = {ip}
            IP in binary = 
            {ip_list[0]:0}    {ip_list[1]:8}    {ip_list[2]:4}    {ip_list[3]:8}
            {ip_list[0]:08b}  {ip_list[1]:08b}  {ip_list[2]:08b}  {ip_list[3]:08b}
           '''
print("Задание 4.8 => \n",ip_print)