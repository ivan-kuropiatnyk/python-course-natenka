'''
Python for network engineers Natasha Samoilenko
'''
# Page range 155
# TASK 6.1
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for mac_i in mac:
    mac_i = mac_i.replace(":",".").upper()
    result.append(mac_i)
print(result)

#task 6.2
'''
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
• «unicast» - если первый байт в диапазоне 1-223
• «multicast» - если первый байт в диапазоне 224-239
• «local broadcast» - если IP-адрес равен 255.255.255.255
• «unassigned» - если IP-адрес равен 0.0.0.0
• «unused» - во всех остальных случаях
'''
ip_address = input("Enter ip address in a format 10.1.1.1: ")
#ip_address = "0.0.0.0"
ip_list = list(ip_address.split("."))
ip_1oct = int(ip_list[0])
ip_2oct = int(ip_list[1])
ip_3oct = int(ip_list[2])
ip_4oct = int(ip_list[3])
unicast = "unicast"
multicast = "multicast"
local_broadcast = "local broadcast"
unassigned = "unassigned"
unused = "unused"
if ip_1oct in range(1,224):
    print(f"IP address {ip_address} is {unicast}")
elif ip_1oct in range(224, 240):
    print(f"IP address {ip_address} is {multicast}")
elif ip_1oct == 255 and ip_2oct == 255 and ip_3oct == 255 and ip_4oct == 255:
    print(f"IP address {ip_address} is {local_broadcast}")
elif ip_1oct == 0 and ip_2oct == 0 and ip_3oct == 0 and ip_4oct == 0:
    print(f"IP address {ip_address} is {unassigned}")
else:
    print(f"IP address {ip_address} is {unused}")